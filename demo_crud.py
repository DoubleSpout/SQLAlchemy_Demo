# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from sqlalchemy import *
from datetime import datetime
import sqlalchemy.types
from demo_define_table import user_table

stmt = user_table.insert(values=dict(user_name=u'富士达1', password=u'富士达1', email_address=u'Rick 富士达1'))
stmt.execute()

stmt = user_table.insert()
stmt.execute(user_name=u'富士达', password=u'富士达', email_address=u'Rick 富士达')

stmt = user_table.update(
 whereclause=text("user_name='富士达'"),
 values=dict(password=u'passwd'))
stmt.execute()

stmt = user_table.update(
 text("user_name='富士达1'"))
stmt.execute(password=u'passwd1')

#子查询更新
#msrp = select(
# [product_table.c.msrp],
# product_table.c.sku==product_price_table.c.sku,
# limit=1)
#stmt = product_price_table.update( values=dict(price=msrp))
#stmt.execute()

stmt = user_table.delete(
    text("user_name='富士达'"))
stmt.execute()


#SQL查询接口
#The select( ) function versus the select( ) method
#使用select函数
stmt = select([user_table.c.user_name])
for row in stmt.execute():
    print row

#使用select方法
stmt = user_table.select()
for row in stmt.execute():
    print row

#select参数：
#columns=None，表示要查找的列名
#bind=None，数据库引擎，如果忽略这个设置，将会使用本表的绑定引擎
#whereclause=None，where的条件，
#from_obj=[]，设置from的条件，如果忽略它，那么将会由SQLAlchemy自动根据其他条件得出
#order_by=None，排序条件
#group_by=None，分组条件
#having=None，having要素
#distinct=False，增加distinct筛选
#for_update=False，增加一个FOR UPDATE筛选，像mysql可以使用‘read’用来锁住表，保证接下来的update准确性
#limit=None，限制行数
#offset=None，偏移量
#correlate=True，是否关联查询
#use_labels=False，对列名数组生成唯一的标签，防止列名冲突
#prefixes=None，将一数组的命令插入到SELECT关键字后和列名前

#where子句
#用来构建where子句，我们可以使用text或者SQL 表达式语法。最简单的方法用来生成where子句就是使用SQLAlchemy提供的操作

stmt=user_table.select(user_table.c.user_name==u"富士达1")
print stmt.execute().fetchall()
















