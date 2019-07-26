from sanic import Blueprint
from apps.users.views.v1 import UserList


bp = Blueprint('users', url_prefix='/api/v1')
bp.add_route(UserList.as_view(), '/users')
