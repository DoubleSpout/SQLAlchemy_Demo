# -*- coding: utf-8 -*-

from sqlalchemy import *
from datetime import datetime
import sqlalchemy.types

metadata = MetaData()
__engine = create_engine('mysql://root:@192.168.150.3/test', connect_args={'charset': 'UTF8'}, echo=True,
                         encoding='UTF-8')
#直接绑定 engine 的MetaData bound_meta = MetaData('sqlite:///test2.db')
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

#Table 类Table.__init__(self, name, metadata,*args, **kwargs)
#name 表名
#metadata 共享的元数据
#*args Column列定义
#**kwargs
#schema 此表的结构名称，默认None
#autoload 自动从现有表中读入表结构，默认False
#autoload_with 从其他engine读取结构，默认None
#例： db = create_engine('sqlite:///devdata.sqlite')
#   brand_table = Table('brand', metadata, autoload=True, autoload_with=db)

#include_columns 如果autoload设置为True，则此项数组中的列明将被引用，没有写的列明将被忽略，None表示所有都列明都引用，默认None
#mustexist 如果为True，表示这个表必须在其他的python应用中定义，必须是metadata的一部分，默认False
#useexisting 如果为True，表示这个表必须被其他应用定义过，将忽略结构定义，默认False
#owner 表所有者，用于Orcal，默认None
#quote 设置为True，如果表明是SQL关键字，将强制转义，默认False
#quote_schema 设置为True，如果列明是SQL关键字，将强制转义，默认False
#mysql_engine mysql专用，可以设置'InnoDB'或'MyISAM'


#Column类定义
#Column.__init__(self,  name,  type_,  *args,  **kwargs)
#name 列名
#type_ 类型，更多类型 sqlalchemy.types
#*args Constraint（约束）,  ForeignKey（外键）,  ColumnDefault（默认）, Sequenceobjects（序列）定义
#key 列明的别名，默认None
#**kwargs
#primary_key 如果为True，则是主键
#nullable 是否可为Null，默认是True
#default 默认值，默认是None
#index 是否是索引，默认是True
#unique 是否唯一键，默认是False
#onupdate 指定一个更新时候的值，这个操作是定义在SQLAlchemy中，不是在数据库里的，当更新一条数据时设置，大部分用于updateTime这类字段
#autoincrement 设置为整型自动增长，只有没有默认值，并且是Integer类型，默认是True
#quote 如果列明是关键字，则强制转义，默认False


#约束定义，可以同时在列声明和表声明中进行
#product_table = Table(
# 'product', metadata,
# Column('brand_id', Integer, ForeignKey('brand.id'),primary_key=True),
# Column('sku', Unicode(80), primary_key=True))
#或者
#product_table = Table(
#  'product', metadata,
#  Column('brand_id', Integer, ForeignKey('brand.id')), Column('sku', Unicode(80)),
#  PrimaryKeyConstraint('brand_id', 'sku', name='prikey'))


#外键的定义
#ForeignKey类
#ForeignKey.__init__(  self,  col-umn,  constraint=None,  use_alter=False,  name=None,  onupdate=None,  ondelete=None)

#唯一定义
#Unique类
#product_table = Table(
#'product', metadata,
#Column('id', Integer, primary_key=True),
#Column('brand_id', Integer, ForeignKey('brand.id')),
#Column('sku', Unicode(80)),
#UniqueConstraint('brand_id', 'sku'))

#检查约束
#CheckConstraints 类
#例子：
#payment_table = Table(
# 'payment', metadata,
# Column('amount', Numeric(10,2), CheckConstraint('amount > 0')))
# Column('original', Numeric(10,2), CheckConstraint('original> 0')),
# Column('discounted', Numeric(10,2),
# CheckConstraint('discounted > 0')),
# CheckConstraint('discounted < original', name='check_constraint_1'))

#index 对象，索引对象
#1、定义多列复合索引
#2、对索引命名
#3、独立的对表创建索引，一般用于已经存在的表，增加索引
# 使用例子
# i = Index('idx_name', user_table.c.first_name,
# user_table.c.last_name, unique=True)
# i.create(bind=e)






metadata.create_all()

stmt = user_table.insert()
stmt.execute(user_name=u'富士达', password=u'富士达', email_address=u'Rick 富士达')
