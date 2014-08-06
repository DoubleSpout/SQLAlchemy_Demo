# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import *

from demo_connect import user_table,group_table,permission_table

#定义3个类
class User(object): pass
class Group(object): pass
class Permission(object): pass

#建立对象和表的映射
mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)

#创建Session和session实例
Session = sessionmaker()
session = Session()

#简单查找
query = session.query(User)
print list(query)
print query.get(1)

#使用 filter_by 进行查找
for user in query.filter_by(display_name='Rick Copeland'):
    print user.id, user.user_name, user.password

#使用 filter 进行查找，注意这里的 User类的c属性，是mapper时候加上的，存储了表的列
for user in query.filter(User.c.user_name.like('rick%')):
    print user.id, user.user_name, user.password

#通过实例化User类，插入数据库
newuser = User()
newuser.user_name = 'mike'
newuser.password = 'password'
session.save(newuser)
#执行save操作后，并没有更新到数据库

#更新第一条记录
rick = query.get(1)
rick.display_name = 'Richard'

#查看当前个数
#query = session.query(User)
print query.count()

#执行flush操作，将数据更新到数据库
session.flush()

#query = session.query(User)
print query.count()

#删除某一个对象
session.delete(newuser)
#提交这个delete
session.commit()