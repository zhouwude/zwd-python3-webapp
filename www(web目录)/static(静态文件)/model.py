#!/usr/bin/env python3

import sys
print(sys.path)

from orm import Model, StringField, IntegerField
# import orm
#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
#内置函数dir()不仅可以 找到某个对象所有属性和方法 还能输出 某个模块得所有属性和方法
print(dir())
# class User(Model):
#     __table__ = 'users' # 设置表名称
#
#     id = IntegerField(primary_key=True)
#     name = StringField()

# 创建实例:
# user = User(id=123, name='Michael')
# # 存入数据库:
# user.insert()
# # 查询所有User对象:
# users = User.findAll()
