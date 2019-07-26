from sanic import Sanic
from apps.users.views import bp as user_bp
from apps.home import bp as home_bp


def init_listeners(app: Sanic, config):
    @app.listener('before_server_start')
    async def init_db(app, loop):
        pass

    @app.listener('after_server_stop')
    async def cleanup_db(app, loop):
        pass


def init_blueprints(app: Sanic):
    app.blueprint(home_bp)
    app.blueprint(user_bp)


def init_middlewares(app: Sanic, config):
    pass


def init_exception_handlers(app: Sanic, config):
    pass


def create_app(config):
    app = Sanic(__name__)

    init_listeners(app=app, config=config)
    init_blueprints(app=app)
    init_middlewares(app=app, config=config)
    init_exception_handlers(app=app, config=config)

    return app
