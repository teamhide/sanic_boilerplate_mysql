from typing import Union, NoReturn
from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import json
from core.exceptions import ValidationErrorException
from apps.users.schemas import CreateUserRequestSchema, UserResponseSchema
from apps.users.dtos import CreateUserDto
from apps.users.interactors import CreateUserInteractor


class UserList(HTTPMethodView):
    decorators = []

    async def get(self, request: Request) -> Union[json, NoReturn]:
        return json(body={'status': True})

    async def post(self, request: Request) -> Union[json, NoReturn]:
        validator = CreateUserRequestSchema().load(data=request.form)
        if validator.errors:
            raise ValidationErrorException
        dto = CreateUserDto(**validator.data)
        user = await CreateUserInteractor().execute(dto=dto)
        schema = UserResponseSchema().dump(user).data
        return json(body={'data': schema})
