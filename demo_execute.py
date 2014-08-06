# -*- coding: utf-8 -*-
from sqlalchemy import *
__engine = create_engine('mysql://root:@192.168.150.3/test',convert_unicode=True, echo=True)

#conn 是DB-API连接对象
conn = __engine.connect()
#result是数据库游标
result = conn.execute('select * from tf_user')
for row in result:
    print row

#result是ResultProxy的实例，具有如下方法
#__iter__() 可迭代
#fetchone() 获取第一行数据，返回类型 RowProxy
#fetchall() 获取所有的数据，返回类型  RowProxy 数组
#scalar() 从游标获取下一行数据
#keys 属性，返回列明的数组
#rowcount 属性，返回记录数
#close() 关闭连接，将连接返回连接池

# RowProxy 类型
#__getattr__() 可以通过 object.column_name 获取值
#__getitem__() 可以通过 object[column_name] 或者 object[column_position] 获取值
#keys() 提供所有 column_name 的数组
#values() 提供所有 value 值的数组
#items() 提供一个 元组(column_name,value)的数组


conn.close()