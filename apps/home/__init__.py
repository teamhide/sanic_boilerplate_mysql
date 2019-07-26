from sanic import Blueprint
from apps.home.home_view import Home


bp = Blueprint('home')
bp.add_route(Home.as_view(), '/')
