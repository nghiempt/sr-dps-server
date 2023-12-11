from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta

category = Table(
    'dps_category', meta,
    Column('category_id', Integer, primary_key=True, autoincrement=True),
    Column('category_name', String(50)),
    Column('category_thumbnail', Text),
    Column('category_key', Text)
)
