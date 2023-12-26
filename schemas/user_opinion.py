from pydantic import BaseModel
from models._index import user_opinion
from datetime import date

class UserOpinion(BaseModel):
    # user_name: str
    # user_email: str
    user_id: int
    app_id: int
    score: int
    date: date
    user_note: str


