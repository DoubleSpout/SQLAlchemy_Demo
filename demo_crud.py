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
#whereclause(whereclause)=None，where的条件，
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

#where操作符
#>>> print product_price_table.c.price == 12.34
#product_price.price = ?
#>>> print product_price_table.c.price != 12.34
#product_price.price != ?
#>>> print product_price_table.c.price < 12.34
#product_price.price < ?
#>>> print product_price_table.c.price > 12.34
#product_price.price > ?
#>>> print product_price_table.c.price <= 12.34
#product_price.price <= ?
#>>> print product_price_table.c.price >= 12.34
#product_price.price >= ?
#>>> print product_price_table.c.price == None
#product_price.price IS NULL

#AND OR NOT
#print (product_table.c.msrp > 10.00) & (product_table.c.msrp < 20.00)
#print and_(product_table.c.msrp > 10.00, product_table.c.msrp < 20.00)
#print product_table.c.sku.like('12%')
#print not_(and_(product_table.c.msrp > 10.00, product_table.c.msrp < 20.00))

#其他条件操作符
#between(cleft, cright)，在这个区间内
#distinct()，distinct操作
#startswith(other)，就像'other%'
#endswith(other)，就像'%other'
#in_(*other)，也可以是子查询，或者一个数组
#like(other)，like操作
#op(operator)，操作
#label(name)，别名，相当于给列 as 名字

#绑定查询条件，加速查询，简洁代码，例子如下：
#stmt = select([product_table.c.msrp], whereclause=product_table.c.sku==bindparam('sku'))
#print stmt.execute(sku='123').fetchall()
#[(12.34,)]
#print stmt.execute(sku='456').fetchall()
#[(22.120000000000001,)]
#print stmt.execute(sku='789').scalar()
#41.44

#bindparam函数的参数说明
#key，绑定的列名
#value=None，默认列名的值
#type=None，绑定的类型
#shortname=None，列名别名
#unique=False，产生所绑定的列名是唯一名称，通常伴随 value 参数一起使用

#使用字符串条件
#stmt = select(['product.msrp'],
#   from_obj=['product'],
#   whereclause=text("product.sku=='123'"))


#排序order，分组groupby和消除重复distinct
#排序
#stmt = product_table.select(order_by=[product_table.c.msrp])
#stmt = product_table.select(order_by=[desc(product_table.c.msrp)])

#groupby 然后 count
#stmt = select([product_price_table.c.sku,
#   func.count(product_price_table.c.store_id)],
#   group_by=[product_price_table.c.sku])
#另外一个having的例子
#>>> stmt = select([product_price_table.c.sku,
#   func.count(product_price_table.c.store_id)],
#   group_by=[product_price_table.c.sku],
#   having=func.count(product_price_table.c.store_id)

#distinct的例子
#stmt = select([product_price_table.c.sku,
#   product_price_table.c.price],
#   distinct=True)

#分页使用，limit和offset的例子
#stmt = product_table.select(offset=1, limit=1)


#多表联合查询，前提是先定义好外键
#1、创建from的对象
#from_obj = store_table.join(product_price_table)
#   .join(product_table)
#query = store_table.select()
#query = query.select_from(from_obj)
#query = query.where(product_table.c.msrp
#   != product_price_table.c.price)
#print query
#SELECT store.id, store.name
#FROM store JOIN product_price ON store.id = product_price.store_id
#   JOIN product ON product.sku = product_price.sku
#   WHERE product.msrp != product_price.price
#print query.column('product.sku')

#整合在一句里面的例子
# query2 = select([store_table, product_table.c.sku],
#   from_obj=[from_obj],
#   whereclause=(product_table.c.msrp
#   !=product_price_table.c.price))
# print query2
#SELECT store.id, store.name, product.sku
#FROM store JOIN product_price ON store.id = product_price.store_id
#JOIN product ON product.sku = product_price.sku
#WHERE product.msrp != product_price.price

#outerjoin的例子
# from_obj = store_table.outerjoin(product_price_table)
# from_obj = from_obj.outerjoin(product_table)
# query = store_table.select()
# query = query.select_from(from_obj)
# query = query.column('product.msrp')
# print query
#SELECT store.id, store.name, product.msrp
#FROM store LEFT OUTER JOIN product_price
# ON store.id = product_price.store_id
# LEFT OUTER JOIN product
# ON product.sku = product_price.sku

#set 操作符 UNION, INTERSECT, EXCEPT
#union(),  union_all(),
#intersect(),  intersect_all(),
#except_(), and  except_all()

#下面2个语句是等价的
#query = product_table.select(and_(product_table.c.msrp > 10.00 , product_table.c.msrp < 20.00))
#query0 = product_table.select(product_table.c.msrp > 10.00)
#query1 = product_table.select(product_table.c.msrp < 20.00)
#query = intersect(query0, query1)


#Subqueries 子查询
#in_操作符
#subquery = select([employee_table.c.id],
#employee_table.c.manager_id==None)
#stmt = employee_table.select(
#   and_(employee_table.c.id.in_(subquery),
#   employee_table.c.name.like('Ted%')))
#print stmt



















