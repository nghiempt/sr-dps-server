from pydantic import BaseModel
from models._index import dspp

class DSPP(BaseModel):
    app_id: int
    app_data_safety: str
    app_privacy_policy: str

    # @property
    # def app_data_safety(self):
    #     return self.app_data_safety

    # @app_data_safety.setter
    # def app_data_safety(self, value):
    #     self.app_data_safety = value
