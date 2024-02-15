from litestar import Litestar, get
from pony.orm import Database, db_session, commit, select
from models import User
from typing import List, Dict, Any
from litestar.config.cors import CORSConfig
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
    if not users:
        print("no users")
        User(username="test")
        commit()
        users = select(u for u in User)
        print(users)

    return [user.to_dict() for user in users]

app = Litestar(route_handlers=[users], cors_config=cors_config)