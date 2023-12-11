from config.db import meta, engine
from models.response_object import ResponseObject

from models.category import category
from models.app import app
from models.user import user
from models.user_opinion import user_opinion
from models.dspp import dspp


# Create/Update all table
meta.create_all(engine)