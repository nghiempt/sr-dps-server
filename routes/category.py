from fastapi import APIRouter, Depends
from models._index import category, app, ResponseObject
# from config.db import conn
from config.db import get_db
from schemas._index import Category
import http.client as HTTP_STATUS_CODE
from sqlalchemy import select, func, join
from sqlalchemy.orm import Session

categoryRouter = APIRouter(prefix="/api/v1")

@categoryRouter.get('/category/get-all')
async def get_all_category(db: Session = Depends(get_db)):
    query = (
        select(category, func.count().label("total_app"))
        .select_from(join(category, app, category.c.category_id == app.c.category_id, isouter=True))
        .group_by(category.c.category_id)
    )

    categories = db.execute(query).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not categories:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "No category found")
    return ResponseObject(True, status_code, status_message, Category.serializeList(categories))
