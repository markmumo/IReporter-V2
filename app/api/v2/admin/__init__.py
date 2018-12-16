from flask import Blueprint

from app.api.v2.admin.views import Admin_Get_incident_by_id


admin_blueprint = Blueprint("admin", __name__)
