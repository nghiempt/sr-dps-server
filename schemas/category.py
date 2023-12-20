from pydantic import BaseModel
from models._index import category

class Category(BaseModel):
    category_id: int
    category_name: str
    category_thumbnail: str
    category_key: str
    
    def serializeList(list):
        # Define keys for your dictionary
        keys = ['category_id', 'category_name', 'category_thumbnail', 'category_key', 'total_app']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values[:5])) for values in list]
        return result
