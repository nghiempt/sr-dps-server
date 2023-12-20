from pydantic import BaseModel
from models._index import user_opinion

class UserOpinion(BaseModel):
    # user_name: str
    # user_email: str
    user_id: int
    app_id: int
    score: int


