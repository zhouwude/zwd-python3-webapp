#!/usr/bin/env python3

import sys
print(sys.path)

from orm import Model, StringField, IntegerField


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