from fastapi import APIRouter
from models._index import user_opinion, user, ResponseObject
from config.db import conn
from schemas._index import UserOpinion
import http.client as HTTP_STATUS_CODE
from typing import List

userOpinionRouter = APIRouter(prefix="/api/v1")

@userOpinionRouter.post('/user-opinion/submit-user-opinion')
async def submit_user_opinion(opinions: List[UserOpinion]):
    # user_id = 0
    for opinionInput in opinions:
        # foundUser = conn.execute(user.select()
        #              .where((user.c.user_name == opinionInput.user_name) & (user.c.user_email == opinionInput.user_email))).fetchone()
        
        # if not foundUser:
        #     result = conn.execute(user.insert().values(
        #         user_name=opinionInput.user_name,
        #         user_email=opinionInput.user_email
        #     ))

        #     user_id = result.lastrowid
        #     conn.execute(user_opinion.insert().values(
        #         user_id=user_id,
        #         app_id=opinionInput.app_id,
        #         score=opinionInput.score
        #     ))
        # else:
            foundOpinion = conn.execute(user_opinion.select()
                        .where((user_opinion.c.user_id == opinionInput.user_id) & (user_opinion.c.app_id == opinionInput.app_id))).fetchone()
        
            if not foundOpinion:
                conn.execute(user_opinion.insert().values(
                    user_id=opinionInput.user_id,
                    app_id=opinionInput.app_id,
                    score=opinionInput.score
                ))
            else:
                conn.execute(user_opinion.update()
                            .where((user_opinion.c.user_id == opinionInput.user_id) & (user_opinion.c.app_id == opinionInput.app_id))
                            .values(score=opinionInput.score))

    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, 'none')

@userOpinionRouter.get('/user-opinion/get-opinion-by-user-id-and-app-id')
async def get_opinion_by_user_id_and_app_id(userid: int, appid: int):
    foundOpinion = conn.execute(user_opinion.select()
                .where((user_opinion.c.user_id == userid) & (user_opinion.c.app_id == appid))).fetchone()
        
    if not foundOpinion:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, 'none')
    
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, foundOpinion.score)
