# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#echo true 表示输出sql语句
metadata = MetaData()
__engine = create_engine('mysql://root:@192.168.150.3/test',convert_unicode=True, echo=True, encoding='UTF-8')
metadata.bind = __engine

#定义表对象
#等级表
level_table = Table(
'level', metadata,
Column('id', Integer, primary_key=True),
Column('parent_id', None, ForeignKey('level.id')),
Column('name', String(20)))

#个人分类表
category_table = Table(
'category', metadata,
Column('id', Integer, primary_key=True),
Column('level_id', None, ForeignKey('level.id')),
Column('parent_id', None, ForeignKey('category.id')),
Column('name', String(20)))

product_table = Table(
'product', metadata,
Column('sku', String(20), primary_key=True),
Column('msrp', Numeric))

#产品汇总表
product_summary_table = Table(
'product_summary', metadata,
Column('sku', None, ForeignKey('product.sku'), primary_key=True),
Column('name', Unicode(255)),
Column('description', Unicode(255)))

product_category_table = Table(
'product_category', metadata,
Column('product_id', None, ForeignKey('product.sku'), primary_key=True),
Column('category_id', None, ForeignKey('category.id'), primary_key=True))

region_table = Table(
'region', metadata,
Column('id', Integer, primary_key=True),
Column('name', Unicode(255)))

store_table = Table(
'store', metadata,
Column('id', Integer, primary_key=True),
Column('region_id', None, ForeignKey('region.id')),
Column('name', Unicode(255)))

#产品价格表
product_price_table = Table(
'product_price', metadata,
Column('sku', None, ForeignKey('product.sku'), primary_key=True),
Column('store_id', None, ForeignKey('store.id'), primary_key=True),
Column('price', Numeric, default=0))


#定义数据对象
class Level(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
    def __repr__(self):
       return '<Level %s>' % self.name

class Category(object):
    def __init__(self, name, level, parent=None):
        self.name = name
        self.level = level
        self.parent = parent
    def __repr__(self):
        return '<Category %s.%s>' % (self.level.name, self.name)

class Product(object):
    def __init__(self, sku, msrp, summary=None):
        self.sku = sku
        self.msrp = msrp
        self.summary = summary
        self.categories = []
        self.prices = []
    def __repr__(self):
        return '<Product %s>' % self.sku

class ProductSummary(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return '<ProductSummary %s>' % self.name


class Region(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Region %s>' % self.name


class Store(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Store %s>' % self.name


class Price(object):
    def __init__(self, product, store, price):
        self.product = product
        self.store = store
        self.price = price
    def __repr__(self):
        return '<Price %s at %s for $%.2f>' % (
        self.product.sku, self.store.name, self.price)

metadata.create_all()

mapper(Region, region_table)
r0 = Region(name=u"Northeast")
r1 = Region(name=u"Southwest")

Session = sessionmaker()
session = Session()

session.add(r0)
session.add(r1)
session.flush()

r0.name = u'Northwest'
session.flush()

#exclude_properties
#排除id列名
#mapper(Region, region_table, exclude_properties=['id'])
#使用properties让数据对象属性和表属性进行关联
#mapper(Region, region_table, properties=dict(
#   region_name=region_table.c.name,
#   region_id=region_table.c.id))