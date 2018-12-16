from flask import Blueprint

from app.api.v2.main.views import PostIncidents, AllIncidents, Get_incident_by_id


views_blueprint = Blueprint("views", __name__)
