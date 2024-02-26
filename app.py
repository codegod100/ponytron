from litestar import Litestar, get, post
from pony.orm import Database, db_session, commit, select
from models import User, Message, Chat
from typing import List, Dict, Any
from litestar.config.cors import CORSConfig
from passlib.hash import pbkdf2_sha256
from litestar.handlers.websocket_handlers import websocket_listener
import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
db = Database()




cors_config = CORSConfig(allow_origins=["*"], allow_methods=["GET", "POST"])




@get("/users")
async def users() -> List[Any]:
    with db_session:
        users = select(u for u in User)
        print(users.show())
        return [user.to_dict() for user in users]


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
        messages = select(m for m in Message if m.chat == chat)
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


@post("/submit_chat")
async def submit_chat(data: Any) -> None:
    with db_session:
        print(data)
        chat = select(c for c in Chat if c.name == data["chat_name"]).first()
        user = select(u for u in User if u.username == data["user"]).first()
        Message(author=user, chat=chat, body=data["body"])
        commit()
        await sio.emit("new_message")


app = Litestar(
    route_handlers=[users, chat, submit_chat, create_user, chats, create_chat],
    cors_config=cors_config,
    debug=True
)
app = socketio.ASGIApp(sio,app)

