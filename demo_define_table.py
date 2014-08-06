# -*- coding: utf-8 -*-

from sqlalchemy import *
from datetime import datetime
import sqlalchemy.types

metadata = MetaData()
__engine = create_engine('mysql://root:@192.168.150.3/test', connect_args={'charset': 'UTF8'}, echo=True,
                         encoding='UTF-8')
metadata.bind = __engine

user_table = Table(
    'tf_user2', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_name', Unicode(16, collation='utf8_bin'), unique=True, nullable=False),
    Column('email_address', Unicode(255, collation='utf8_bin'), unique=True, nullable=False),
    Column('password', Unicode(40, collation='utf8_bin'), nullable=False),
    Column('first_name', Unicode(255, collation='utf8_bin'), default=u'发'),
    Column('last_name', Unicode(255, collation='utf8_bin'), default=u'发'),
    Column('created', DateTime, default=datetime.now)
)

metadata.create_all()