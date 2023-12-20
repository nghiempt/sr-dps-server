from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, Date
from config.db import meta

user = Table(
    'dps_user', meta,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(100)),
    Column('user_email', String(100)),
    Column('user_role', Text),
    Column('user_level', Text)
)
