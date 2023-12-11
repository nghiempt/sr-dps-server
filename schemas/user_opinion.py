from pydantic import BaseModel
from models._index import user_opinion
from config.db import conn

class UserOpinion(BaseModel):
    # user_name: str
    # user_email: str
    user_id: int
    app_id: int
    score: int


