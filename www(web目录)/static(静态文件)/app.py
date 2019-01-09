import  logging; logging.basicConfig(level=logging.INFO) #单行存在多条python语句的话 用逗号隔开。

import  json, os, time, asyncio

from aiohttp import  web

from datetime import  datetime, timedelta

async def index(request):
    # await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def hello(request):
    # await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index),
                web.get('/{name}', hello)])

web.run_app(app=app, host='127.0.0.1',port=9000) #127.0.0.1 和 localhost 是一样的。



