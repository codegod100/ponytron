import json
from litestar import Litestar, get, post, Request, Response
from pony.orm import Database, db_session, commit, select, desc
from models import User, Message, Chat, Subscription
from typing import List, Dict, Any
from litestar.config.cors import CORSConfig
from passlib.hash import pbkdf2_sha256
import socketio
from dotenv import load_dotenv
import os
import jwt
from atproto import Client, client_utils


clients = {}

load_dotenv()
SECRET = os.environ["SECRET"]
BASE_URL = os.environ["BASE_URL"]

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
db = Database()


cors_config = CORSConfig(allow_origins=["*"], allow_methods=["GET", "POST"])


def decode(j):
    payload = jwt.decode(j, SECRET, algorithms=["HS256"])
    return payload["username"]


@get("/.well-known/webfinger")
async def webfinger(resource: str, request: Request) -> Any:
    jrd = {
        "subject": resource,
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": BASE_URL + "users/v",
            }
        ],
    }
    return jrd


@get("/users/{username:str}")
async def activities(username: str) -> Any:
    with open("activity.json") as f:
        d = json.load(f)
        text = json.dumps(d)
        nt = text.replace("https://federate.social/", BASE_URL)
        return Response(content=nt, media_type="application/activity+json")


@post("/inbox")
async def inbox(data: Any) -> Any:
    print(json.dumps(data))


@get("/users")
async def users() -> List[Any]:
    with db_session:
        users = select(u for u in User)
        print(users.show())
        return [user.to_dict() for user in users]


@get("/user/{username:str}")
async def user(username: str) -> Any:
    with db_session:
        user = select(u for u in User if u.username == username).first()
        if not user:
            user = User(username=username)
            commit()
        return user.to_dict()


@get("/chats")
async def chats() -> List[Any]:
    with db_session:
        chats = select(c for c in Chat)
        out = []
        for c in chats:
            chat = c.to_dict()
            chat["owner"] = c.owner.username
            out.append(chat)
        return out


@post("/chats")
async def create_chat(data: Any) -> None:
    with db_session:
        chats = select(c for c in Chat if c.name == data["name"])
        user = select(u for u in User if u.username == data["owner"]).first()
        if not chats:
            Chat(owner=user, name=data["name"])


@get("/chat/{name:str}")
async def chat(name: str) -> Dict:
    with db_session:
        chat = select(c for c in Chat if c.name == name).first()
        messages = (
            select(m for m in Message if m.chat == chat)
            .order_by(lambda m: desc(m.id))
            .limit(15)
        )
        out = {"name": chat.name, "messages": []}
        for m in messages:
            message = m.to_dict("id body")
            message["author"] = m.author.username
            out["messages"].append(message)
        return out


@post("/create_user")
async def create_user(data: Any) -> None:
    with db_session:
        password = pbkdf2_sha256.hash(data["password"])
        user = select(u for u in User if u.username == data["username"]).first()
        if not user:
            User(username=data["username"], password=password)
            commit()


@post("/login")
async def login(data: Any) -> Any:
    with db_session:
        client = Client()
        profile = client.login(data["username"], data["password"])
        session_string = client.export_session_string()
        name = profile.handle
        user = select(u for u in User if u.username == name).first()
        if not user:
            User(username=name, session=session_string)
            commit()
        encoded = jwt.encode({"username": name}, SECRET, algorithm="HS256")
        return encoded


@post("/submit_chat")
async def submit_chat(data: Any) -> None:
    with db_session:
        chat = select(c for c in Chat if c.name == data["chat_name"]).first()
        user = select(u for u in User if u.username == decode(data["jwt"])).first()
        Message(author=user, chat=chat, body=data["body"])
        commit()
        await sio.emit("new_message")


@post("/subscribe")
async def subscribe(data: Any) -> None:
    with db_session:
        user = select(u for u in User if u.username == data["user"]).first()
        Subscription(user=user, follower=data["my_info"])
        commit()


@post("/unsubscribe")
async def unsubscribe(data: Any) -> None:
    with db_session:
        user = select(u for u in User if u.username == data["user"]).first()
        sub = select(
            s for s in Subscription if s.user == user and s.follower == data["my_info"]
        ).first()
        sub.delete()
        commit()


@get("/subscriptions/{user:str}")
async def subscriptions(user: Any) -> Any:
    with db_session:
        user = select(u for u in User if u.username == user).first()
        return [s.to_dict() for s in user.subscriptions]


@get("/following/{user:str}")
async def following(user: Any) -> Any:
    with db_session:
        subs = select(s for s in Subscription if s.follower == user)
        print(subs.show())
        users = [s.user for s in subs]
        return [u.username for u in users]


@post("/status")
async def status(data: Any) -> Any:
    with db_session:
        print(data)
        username = decode(data["jwt"])
        user = select(u for u in User if u.username == username).first()
        Status(author=user, body=data["body"])
        commit()


@get("/statuses/{username:str}")
async def statuses(username: str, headers: Any) -> Any:
    with db_session:
        print(headers)
        token = headers["authorization"]
        token = token.replace("Bearer ", "")
        session_username = decode(token)
        user = select(u for u in User if u.username == session_username).first()
        client = Client()
        client.login(session_string=user.session)
        profile_feed = client.get_author_feed(actor=username)
        for feed_view in profile_feed.feed:
            # print("-", feed_view.post.record)
            pass
        return [feed_view.post.record for feed_view in profile_feed.feed][:5]


app = Litestar(
    route_handlers=[
        users,
        chat,
        submit_chat,
        create_user,
        chats,
        create_chat,
        subscribe,
        subscriptions,
        following,
        user,
        unsubscribe,
        status,
        statuses,
        login,
        webfinger,
        activities,
        inbox,
    ],
    cors_config=cors_config,
    debug=True,
)
app = socketio.ASGIApp(sio, app)
