from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, Date
from config.db import meta

app = Table(
    'dps_app', meta,
    Column('app_id', Integer, primary_key=True, autoincrement=True),
    Column('app_package_name', String(255)),
    Column('app_name', String(255)),
    Column('app_thumbnail', Text),
    Column('app_description', Text),
    Column('developer', String(255)),
    Column('date_of_analysis', Date),
    Column('number_of_downloads', String(255)),
    Column('data_safety_link', Text),
    Column('privacy_policy_link', Text),
    Column('category_id', Integer, ForeignKey('dps_category.category_id')),
    Column('label', Text),
    Column('label_description', Text)
)
