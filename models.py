from pony.orm import *

db = Database()
db.bind('sqlite', 'data.sql', create_db=True)



class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    display_name = Optional(str)
    username = Optional(str)
    host = Optional(str)
    avatar = Optional(buffer)


db.generate_mapping(create_tables=True)