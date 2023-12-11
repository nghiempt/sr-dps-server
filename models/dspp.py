from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text
from config.db import meta

dspp = Table(
    'dps_dspp', meta,
    Column('app_id', Integer, ForeignKey('dps_app.app_id'), primary_key=True),
    Column('app_data_safety', Text),
    Column('app_privacy_policy', Text)
)