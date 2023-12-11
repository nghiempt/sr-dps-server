from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

connect_db_string = os.getenv("CONNECT_DB_STRING")
engine = create_engine(connect_db_string, echo=True)

meta = MetaData()
conn = engine.connect()