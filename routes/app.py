from fastapi import APIRouter, Depends
from models._index import app, dspp, user_opinion, ResponseObject
# from config.db import conn
from config.db import get_db
from schemas._index import App
import http.client as HTTP_STATUS_CODE
from helper_function.make_final_dataset_only_prompt import READ_DATA_SAFETY
from helper_function.make_final_dataset_only_prompt import READ_PRIVACY_POLICY
from sqlalchemy import select, func, literal_column, and_, or_
import json
from sqlalchemy.orm import Session

appRouter = APIRouter(prefix="/api/v1")

@appRouter.get('/app/get-by-category-id')
async def get_app_by_category_id(CategoryID: int, UserID: int, db: Session = Depends(get_db)):
    joined_query = app.join(dspp, app.c.app_id == dspp.c.app_id, isouter=True).join(user_opinion, app.c.app_id == user_opinion.c.app_id, isouter=True)
    select_statement = select(app, func.coalesce(user_opinion.c.score, literal_column('0')).label('score'), dspp.c.app_data_safety, dspp.c.app_privacy_policy).select_from(joined_query).where(and_(app.c.category_id == CategoryID, or_(user_opinion.c.user_id == UserID, user_opinion.c.user_id.is_(None))))
    apps = db.execute(select_statement).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not apps:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No app found")
    
    apps_dicts = [dict(row._mapping) for row in apps]
    for row in apps_dicts:
        if row['app_data_safety']:
            row['app_data_safety'] = json.loads(row['app_data_safety'])
        if row['app_privacy_policy']:
            if row['app_privacy_policy'].startswith("{"):     
                row['app_privacy_policy'] = json.loads(row['app_privacy_policy'])
        if row['label']:
            row['label'] = json.loads(row['label'])
        if row['label_description']:
            row['label_description'] = json.loads(row['label_description'])

    return ResponseObject(True, status_code, status_message, apps_dicts)

# @appRouter.get('/app/get-app-data-safety/{URL:path}')
# async def get_app_data_safety(URL: str):
#     preprocess_datasafety = await READ_DATA_SAFETY().scrape_link(URL)
    
#     result = READ_DATA_SAFETY().formated_data_string_only(preprocess_datasafety)
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, result)

# @appRouter.get('/app/get-app-privacy-policy/{URL:path}')
# async def get_app_privacy_policy(URL: str):
#     result = READ_PRIVACY_POLICY().generate_result_string_only(URL)
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     if result == "No provide sharing information section":
#         return ResponseObject(True, status_code, status_message, result)
#     # data_dict = json.loads(result)
#     return ResponseObject(True, status_code, status_message, result)