#!/usr/bin/env python3

import sys
print(sys.path)

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField, create_pool


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

# id 唯一标识符 value 值 type 类型  对象三要素

# 时间戳 加 uuid 一起
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments' #class 属性

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)




sqlInfo = {
    'host': "localhost",
    'password':"@mb1314love",
    'db':'awesome',
}
import  asyncio


async  def test():
    loop = asyncio.get_event_loop()
    await create_pool(loop,**sqlInfo)
    use = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await use.save()

    return "done"



t = test() #coroutine object
print(t)
try:
   r =  t.send(None)
   print('--------%s' % r)
except StopIteration as a:
    print(a.value)


# async