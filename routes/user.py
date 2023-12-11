from fastapi import APIRouter
from models._index import user, ResponseObject
from config.db import conn
from schemas._index import User
import http.client as HTTP_STATUS_CODE

userRouter = APIRouter(prefix="/api/v1")

@userRouter.post('/user/save-user')
async def save_user(userInput: User):
    conn.execute(user.insert().values(
        user_name=userInput.user_name,
        user_email=userInput.user_email
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, 'none')
