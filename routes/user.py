from fastapi import APIRouter, Depends
from models._index import user, ResponseObject
# from config.db import conn
from config.db import get_db
from schemas._index import User
import http.client as HTTP_STATUS_CODE
from sqlalchemy import select
from sqlalchemy.orm import Session

userRouter = APIRouter(prefix="/api/v1")

@userRouter.post('/user/save-user')
async def save_user(userInput: User, db: Session = Depends(get_db)):
    foundUser = db.execute(user.select()
                .where((user.c.user_name == userInput.user_name) & (user.c.user_email == userInput.user_email))).fetchone()
    if foundUser:
        status_code = HTTP_STATUS_CODE.OK
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, User.serializeObject(foundUser))
    else:
        result = db.execute(user.insert().values(
            user_name=userInput.user_name,
            user_email=userInput.user_email
        ))

        user_id = result.lastrowid
        select_query = select(user).where(user.c.user_id == user_id)
        inserted_user = db.execute(select_query).fetchone()

        db.commit()

        status_code = HTTP_STATUS_CODE.CREATED
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, User.serializeObject(inserted_user))

