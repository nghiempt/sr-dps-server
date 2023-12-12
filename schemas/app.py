from pydantic import BaseModel
from models._index import app, category
from config.db import conn
from datetime import date

class App(BaseModel):
    app_id: int
    app_package_name: str
    app_name: str
    app_thumbnail: str
    app_description: str
    developer: str
    date_of_analysis: date
    number_of_downloads: str
    data_safety_link: str
    privacy_policy_link: str
    category_id: int
    label: str
    label_description: str
    
    def serializeList(list):
        keys = ['app_id', 'app_package_name', 'app_name', 'app_thumbnail', 'app_description', 'developer', 'date_of_analysis', 'number_of_downloads', 'data_safety_link', 'privacy_policy_link', 'category_id', 'label', 'label_description']

        result = [dict(zip(keys, values[:13])) for values in list]
        return result
