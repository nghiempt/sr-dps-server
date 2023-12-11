from pydantic import BaseModel
from models._index import user
from config.db import conn

class User(BaseModel):
    user_name: str
    user_email: str
