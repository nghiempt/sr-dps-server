from pydantic import BaseModel
from models._index import user

class User(BaseModel):
    user_name: str
    user_email: str

    def serializeObject(user):
        keys = ['user_id', 'user_name', 'user_email']

        values = [getattr(user, key) for key in keys]

        result = dict(zip(keys, values))
        return result