from fastapi import APIRouter
from models._index import app, dspp, ResponseObject
from config.db import conn
from schemas._index import App
import http.client as HTTP_STATUS_CODE
from helper_function.make_final_dataset_only_prompt import READ_DATA_SAFETY
from helper_function.make_final_dataset_only_prompt import READ_PRIVACY_POLICY
from urllib.parse import unquote
from sqlalchemy import select
import json

appRouter = APIRouter(prefix="/api/v1")

@appRouter.get('/app/get-app-by-category-id/{ID}')
async def get_app_by_category_id(ID: int):
    joined_query = app.join(dspp, app.c.app_id == dspp.c.app_id, isouter=True)
    select_statement = select(app, dspp.c.app_data_safety, dspp.c.app_privacy_policy).select_from(joined_query).where(app.c.category_id == ID)
    apps = conn.execute(select_statement).fetchall()

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
            row['app_privacy_policy'] = json.loads(row['app_privacy_policy'])
        if row['label']:
            row['label'] = json.loads(row['label'])
        if row['label_description']:
            row['label_description'] = json.loads(row['label_description'])

    return ResponseObject(True, status_code, status_message, apps_dicts)

# @appRouter.get('/app/get-app-data-safety/{URL:path}')
# async def get_app_data_safety(URL: str):
#     preprocess_datasafety = await READ_DATA_SAFETY().scrape_link(URL)
    
#     result = READ_DATA_SAFETY().formated_data(preprocess_datasafety)
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, result)

@appRouter.get('/app/get-app-privacy-policy/{URL:path}')
async def get_app_privacy_policy(URL: str):
    result = READ_PRIVACY_POLICY().generate_result(URL)
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    if result == "No provide sharing information section":
        return ResponseObject(True, status_code, status_message, result)
    data_dict = json.loads(result)
    return ResponseObject(True, status_code, status_message, data_dict)