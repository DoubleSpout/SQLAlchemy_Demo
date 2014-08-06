# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime

#echo true 表示输出sql语句
metadata = MetaData()
__engine = create_engine('mysql://root:@192.168.150.3/test',convert_unicode=True, echo=True, encoding='UTF-8')
#直接绑定 engine 的MetaData bound_meta = MetaData('sqlite:///test2.db')
metadata.bind = __engine


# create_engine 参数
# connect_args 数据库链接参数
# convert_unicode 将保存的unicode字符串数据转为2进制存入数据库，取出时也将2进制取出专程unicode，主要用于数据库不支持Unicode编码使用，默认 False
# creator 一个可以被调用的对象（带有__call__的对象），返回DB-API的链接对象，默认None
# echo 是否输出SQLAlchemy日志，包括拼接的sql语句，默认None
# echo_pool 是否输出连接池日志，从连接池取出或放入，默认None
# encoding 设置传输数据的编码，默认是False
# module 设置使用这个数据库哪一个连接模块，比如某些数据库安装了几个连接模块，默认False
# pool 如果设定，则使用一个已经存在的连接池，不设定表示重新创建一个，默认None
# poolclass 表示这个引擎是否自己实现连接池类，否则会使用 sqlalchemy.pool.QueuePool ，而SQLite会使用 sqlalchemy.pool.SingletonThreadPool，
# 默认 None
# max_overflow 表示连接池允许超出的连接数，默认是10
# pool_size 表示连接池数量，默认是5
# pool_recycle 单位秒，表示将闲置的连接释放掉，对于mysql数据库会自动释放闲置连接，有必要对这个值进行设置
# pool_timeout 从连接池中获取连接的超时时间，单位秒，默认是30
# strategy 为这个连接引擎选择一个别用的策略，当前备用策略包括"threadlocal"和"plain"
# "threadlocal" 在一个线程中重用一个连接，执行多条语句
# "plain" （默认） 对每一条语句使用一个连接
# threaded 仅在Oracle数据库使用，默认False
# use_ansi 仅在Oracle数据库使用
# use_oids 仅在PostgreSQL数据库使用


#用户表
user_table = Table(
'tf_user', metadata,#表名 tf_user
Column('id', Integer, primary_key=True),
Column('user_name', Unicode(16),unique=True, nullable=False),
Column('password', Unicode(40), nullable=False),
Column('display_name', Unicode(255), default=''),
Column('created', DateTime, default=datetime.now)
)

#角色表
group_table = Table(
'tf_group', metadata,
Column('id', Integer, primary_key=True),
Column('group_name', Unicode(16),unique=True, nullable=False)
)

#权限表
permission_table = Table(
'tf_permission', metadata,
Column('id', Integer, primary_key=True),
Column('permission_name', Unicode(16),unique=True, nullable=False)
)

#用户-角色表-关联表
user_group_table = Table(
'tf_user_group', metadata,
Column('user_id', None, ForeignKey('tf_user.id'),primary_key=True),
Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True)
)

#角色-权限表-关联表
group_permission_table = Table(
'tf_group_permission', metadata,
Column('permission_id', None, ForeignKey('tf_permission.id'),primary_key=True),
Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True))

#将表结构更新到，安全操作，会先判断是否存在
metadata.create_all()

#简单插入几条数据
#创建insert对象
stmt = user_table.insert()

#可以重复执行插入操作
stmt.execute(user_name='rick', password='secret',display_name='Rick Copeland')
stmt.execute(user_name='rick1', password='secret',display_name='Rick Copeland Clone')

#进行查询
stmt = user_table.select()
result = stmt.execute()
for row in result:
    print row

#获取一行
stmt = user_table.select()
result = stmt.execute()
row =result.fetchone()
print row['user_name']
print row.password
print row.created

#根据条件获取
stmt = user_table.select(user_table.c.user_name=='rick')
#fetchall将结果转换为数组
print stmt.execute().fetchall()

#根据条件更新
stmt = user_table.update(user_table.c.user_name=='rick')
#执行更新password
stmt.execute(password='secret123')

#根据条件删除
stmt = user_table.delete(user_table.c.user_name != 'rick')
stmt.execute()


