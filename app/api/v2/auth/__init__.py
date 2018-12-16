from flask import Blueprint

from app.api.v2.auth.views import Sign_in, Sign_up


auth_blueprint = Blueprint("auth", __name__)
