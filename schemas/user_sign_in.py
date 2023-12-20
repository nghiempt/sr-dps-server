from pydantic import BaseModel

class UserSignIn(BaseModel):
    user_email: str