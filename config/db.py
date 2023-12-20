from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os

load_dotenv()

connect_db_string = os.getenv("CONNECT_DB_STRING")
engine = create_engine(connect_db_string, echo=True)

meta = MetaData()
# conn = engine.connect()

def get_db():
    db = Session(autocommit=False, bind=engine)
    try:
        yield db
    finally:
        # print("*********** DB CLOSED *************")
        db.close()