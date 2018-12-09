from flask import Flask
from flask_restful import Resource, reqparse
from app.api.v2.models.incidents import Incident, incidents
from app.api.v2.models.users import User, Users


class Incidents(Resource):
    def get(self):
        return {"Incidents": [incident.serializer() for incident in incidents]}


""" get incidents by id """


class Get_incident_by_id(Resource):
    parsing = reqparse.RequestParser()

    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}
        else:
            return {"Incident": incident.serializer()}
    """ change incidents status """

    def patch(self, id):

        data = Get_incident_by_id.parsing.parse_args()

        created_by = data['created_by']
        Type = data['Type']
        location = data['location']
        status = data['status']
        image = data['image']
        comment = data['comment']

        specific_incident = Incident().get_incident_by_id(id)

        if not specific_incident:
            return {"message": "This incident does not exist"}, 404
        else:
            specific_incident.created_by = created_by
            specific_incident.Type = Type
            specific_incident.location = location
            specific_incident.status = status
            specific_incident.image = image
            specific_incident.comment = comment

            return {"Incident": specific_incident.serializer()}, 200


""" get all registered users """


class All_users(Resource):
    def get(self):
        return {"Users": [user.serialize() for user in Users]}


""" get users by their username """


class Get_users_by_email(Resource):
    def get(self, email):

        user = User().get_user_by_email(email)
        if user:
            return {"User": user.serialize()}


""" get users by the id """


class Get_user_by_id(Resource):
    def get(self, id):
        user = User().get_user_by_id(id)
        if not user:
            return{"User does not exist"}
        else:
            return {"User": user.serialize()}
