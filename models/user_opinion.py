from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, Date
from config.db import meta

user_opinion = Table(
    'dps_user_opinion', meta,
    Column('user_id', Integer,  ForeignKey('dbs_user.user_id'), primary_key=True,),
    Column('app_id', Integer,  ForeignKey('dbs_app.app_id'), primary_key=True,),
    Column('score', Integer),
    Column('date', Date),
    Column('user_note', Text)
    
)
