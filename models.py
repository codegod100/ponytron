from pony.orm import *

db = Database()
db.bind("sqlite", "data.sql", create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    display_name = Optional(str)
    username = Optional(str)
    host = Optional(str)
    avatar = Optional(buffer)
    messages = Set("Message")
    chats = Set("Chat")
    subscriptions = Set("Subscription")
    session = Optional(str)


class Subscription(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    follower = Required(str)
    composite_key(user, follower)


class Chat(db.Entity):
    id = PrimaryKey(int, auto=True)
    messages = Set("Message")
    name = Optional(str)
    owner = Required(User)


class Message(db.Entity):
    id = PrimaryKey(int, auto=True)
    chat = Required(Chat)
    body = Optional(str)
    author = Required(User)


db.generate_mapping(create_tables=True)
