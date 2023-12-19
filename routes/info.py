from fastapi import APIRouter
from models._index import user, ResponseObject
from config.db import conn
import http.client as HTTP_STATUS_CODE
from sqlalchemy import select

infoRouter = APIRouter(prefix="/api/v1")

@infoRouter.get('/info/get-project-info')
async def get_project_info():
    result = conn.execute(user.insert().values(
        user_name=userInput.user_name,
        user_email=userInput.user_email
    ))

    user_id = result.lastrowid
    select_query = select(user).where(user.c.user_id == user_id)
    inserted_user = conn.execute(select_query).fetchone()

    conn.commit()

    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, User.serializeObject(inserted_user))

