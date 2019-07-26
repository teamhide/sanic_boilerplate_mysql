from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json


class Home(HTTPMethodView):
    decorators = []

    async def get(self, request: Request) -> json:
        return json(body={'status': True})
