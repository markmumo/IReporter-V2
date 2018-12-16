from functools import wraps
from flask import Flask
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse

from app.api.v2.models import incidents
from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from utils import validators


def admin_only(f):
    ''' Restrict access if not admin '''
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        user = User().get_user_by_username(get_jwt_identity()["username"])
        if not user.is_admin:
            return {'message': 'Unauthorized access, you must be an admin to update this Incident records'}, 401
        return f(*args, **kwargs)
    return wrapper_function


class Incidents(Resource):

    @jwt_required
    @admin_only
    def get(self):
        ''' get all incidents by admin '''

        incidents = Incident().get_all_incidents()

        if not incidents:
            return {"message": "Incidents not found"}, 404

        return {"Incidents": [incident.serializer() for incident in incidents]}, 200


class Admin_Get_incident_by_id(Resource):
    ''' get incidents by id '''
    parser = reqparse.RequestParser()
    parser.add_argument("status", type=str, required=True)

    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}
        else:
            return {"Incident": incident.serializer()}
    """ change incidents status """

    @jwt_required
    @admin_only
    def patch(self, id):

        data = Admin_Get_incident_by_id.parser.parse_args()

        status = data['status']

        specific_incident = Incident().get_by_id(id)

        if not specific_incident:
            return {"message": "This incident does not exist"}, 404

        if specific_incident.status == 'draft':
            return {"message": " "}, 404

        specific_incident.update_status(status, id)

        return {"Incident": specific_incident.serializer()}, 200
