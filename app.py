import json
from litestar import Litestar, get, post
from pony.orm import Database, db_session, commit, select
from models import User, Message, Chat
from typing import List, Dict, Any
from litestar.config.cors import CORSConfig
from passlib.hash import pbkdf2_sha256
db = Database()

cors_config = CORSConfig(
    allow_origins=["*"],
    allow_methods=["GET", "POST"]
)

@get("/")
async def hello_world() -> dict[str, str]:
    """Keeping the tradition alive with hello world."""
    return {"hello": "world"}

@get("/users")
async def users() -> List[Any]:
    users = select(u for u in User)
    print(users.show())
    # if not users:
    #     print("no users")
    #     User(username="test")
    #     commit()
    #     users = select(u for u in User)
    #     print(users)

    return [user.to_dict() for user in users]

@get("/chat/{name:str}")
async def chat(name: str) -> Dict:
    with db_session:
        chat = select(c for c in Chat if c.name == name).first()
        messages = select(m for m in Message if m.chat == chat)
        out = {"name": chat.name, "messages": []}
        for m in messages:
            message = m.to_dict('id body')
            message["author"] = m.author.username
            out["messages"].append(message)
        return out

@post("/create_user")
async def create_user(data: Any) -> None:
    password = pbkdf2_sha256.hash(data["password"])
    user = select(u for u in User if u.username == data["username"]).first()
    if not user:
        User(username=data["username"], password=password)
        commit()

@post("/submit_chat")
async def submit_chat(data: Any) -> None:
    print(data)
    chat = select(c for c in Chat if c.name == data["chat_name"]).first()
    user = select(u for u in User if u.username == data["user"]).first()
    message = Message(author=user, chat=chat, body=data["body"])
    commit()
app = Litestar(route_handlers=[users,chat,submit_chat,create_user], cors_config=cors_config)