from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.api.v2.url import url
from instance.config import config

jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    jwt.init_app(app)

    from app.api.v2 import api_bp as api_blueprint
    api = Api(api_blueprint)

    app.register_blueprint(api_blueprint, url_prefix="/api/v2")


    from app.api.v2.admin import admin_blueprint as admin_blp
    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix="/api/v2")


    from app.api.v2.auth import auth_blueprint as auth_blp
    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix="/api/v2")


    from app.api.v2.main import views_blueprint as views_blp
    user = Api(views_blp)
    app.register_blueprint(views_blp, url_prefix="/api/v2")
    

    url(api)

    return app
