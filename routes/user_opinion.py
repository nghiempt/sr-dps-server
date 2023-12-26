from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from models._index import user_opinion, user, app, ResponseObject
# from config.db import conn
from config.db import get_db
from schemas._index import UserOpinion
import http.client as HTTP_STATUS_CODE
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, and_
import pandas as pd

userOpinionRouter = APIRouter(prefix="/api/v1")

@userOpinionRouter.post('/user-opinion/submit-opinion')
async def submit_user_opinion(opinions: List[UserOpinion], db: Session = Depends(get_db)):
    for opinionInput in opinions:
            foundOpinion = db.execute(user_opinion.select()
                        .where((user_opinion.c.user_id == opinionInput.user_id) & (user_opinion.c.app_id == opinionInput.app_id))).fetchone()
        
            if not foundOpinion:
                foundUserID = db.execute(user.select()
                        .where(user.c.user_id == opinionInput.user_id)).fetchone()
                foundAppID = db.execute(app.select()
                        .where(app.c.app_id == opinionInput.app_id)).fetchone()
                if not foundUserID or not foundAppID:
                    status_code = HTTP_STATUS_CODE.BAD_REQUEST
                    status_message = HTTP_STATUS_CODE.responses[status_code]
                    return ResponseObject(True, status_code, status_message, opinions)
                
                db.execute(user_opinion.insert().values(
                    user_id=opinionInput.user_id,
                    app_id=opinionInput.app_id,
                    score=opinionInput.score,
                    date=opinionInput.date,
                    user_note = opinionInput.user_note
                ))
            else:
                db.execute(user_opinion.update()
                            .where((user_opinion.c.user_id == opinionInput.user_id) & (user_opinion.c.app_id == opinionInput.app_id))
                            .values(score=opinionInput.score))

    db.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, opinions)

@userOpinionRouter.get('/user-opinion/get-opinion')
async def get_opinion_by_user_id_and_app_id(userid: int, appid: int, db: Session = Depends(get_db)):
    foundOpinion = db.execute(user_opinion.select()
                .where((user_opinion.c.user_id == userid) & (user_opinion.c.app_id == appid))).fetchone()
        
    if not foundOpinion:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, 0)
    
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, foundOpinion.score)

@userOpinionRouter.post('/user-opinion/clear-all-score')
async def clear_all_score_by_user_id_and_category_id(userid: int, categoyid: int, db: Session = Depends(get_db)):
    subquery = select(app.c.app_id).where(app.c.category_id == categoyid)
    select_query = (
        select(user_opinion)
        .where(
            and_(
                user_opinion.c.user_id == userid,
                user_opinion.c.app_id.in_(subquery)
            )
        )
    )
    list_opinion = db.execute(select_query).fetchall()
    if not list_opinion:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, "No opinion found")
    else:
        delete_query = (
            delete(user_opinion)
            .where(
                and_(
                    user_opinion.c.user_id == userid,
                    user_opinion.c.app_id.in_(subquery)
                )
            )
        )
        result = db.execute(delete_query)
        db.commit()
        
        status_code = HTTP_STATUS_CODE.OK
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(True, status_code, status_message, "Delete success")
    
@userOpinionRouter.get("/user-opinion/export-to-excel")
async def export_to_excel(db: Session = Depends(get_db)):
        joined_query = user_opinion.join(user, user.c.user_id == user_opinion.c.user_id).join(app, app.c.app_id == user_opinion.c.app_id)
        query = select(user.c.user_id, user.c.user_name, user.c.user_email, app.c.app_name, user_opinion.c.score, user_opinion.c.date, user_opinion.c.user_note).select_from(joined_query)
        results = db.execute(query).fetchall()
        selected_columns = ['user_id', 'user_name', 'user_email', 'app_name', 'opinion', 'date', 'note']
        df = pd.DataFrame(results, columns=selected_columns)
        score_mapping = {
        1: 'Totally Disagree',
        2: 'Disagree',
        3: 'Neutral',
        4: 'Agree',
        5: 'Totally Agree'
        }

        df['opinion'] = df['opinion'].map(score_mapping)
        excel_filename = "exported_table.xlsx"
        df.to_excel("./dataset/survey_result/" + excel_filename, index=False, engine='openpyxl')
        file_path = f"./dataset/survey_result/{excel_filename}"
        return FileResponse(file_path, filename=excel_filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


