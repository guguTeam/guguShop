from sanic import Sanic
from sanic.response import json
from sanic_session import Session, InMemorySessionInterface

import threading

app = Sanic()
session = Session(app, interface=InMemorySessionInterface())


@app.route("/")
async def test(request):
    if not request['session'].get('user'):
        request['session']['user'] = 0
    request['session']['user'] += 1
    return json({"hello": request['session']['user']})


def start():
    threading.Thread(target=lambda : app.run(host='0.0.0.0', port=80), name='web').start()

