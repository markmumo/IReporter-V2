# module import
import pdb

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended.utils import current_user, get_jwt_identity
from flask_restful import Resource, reqparse

from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from utils.validators import Validate


class PostIncidents(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("Type", type=str, required=True)
    parser.add_argument("location", type=str, required=True)
    parser.add_argument("image", type=str, required=True)
    parser.add_argument("video", type=str, required=True)
    parser.add_argument("comment", type=str, required=True)

    @jwt_required
    def post(self):

        data = PostIncidents.parser.parse_args()

        Type = data["Type"]
        location = data["location"]
        image = data["image"]
        video = data["video"]
        comment = data["comment"]

        if not Validate.is_string(Type):
            return {"type": "must be a string"}, 400

        created_by = get_jwt_identity()

        print(created_by["username"])

        incident = Incident(
            created_by["username"], Type, location, image, video, comment)

        incident.add()

        return {"Status": '201', 'Data': f'{data}', "Message": 'Incident created successfully'}, 201


class AllIncidents(Resource):

    ''' GET all incidents '''
    @jwt_required
    def get(self):
        created_by = get_jwt_identity()
        incidents = Incident().get_by_requester(created_by['username'])
        if not incidents:
            return {"message": "incidents not found"}, 404

        return {"Status": '200', "Incidents": [incident.serializer() for incident in incidents], "Message": 'Incident fetched successfully'}, 200


class Get_incident_by_id(Resource):

    ''' GET incident by id '''
    @jwt_required
    def get(self, incident_id):
        created_by = get_jwt_identity()

        incident = Incident().get_by_id(incident_id)

        if not incident:

            return {"Status": '404', "Message": "Incident does not exit"}, 404

        else:

            return {"Status": '200', "Incident": incident.serializer(), "Message": 'Incident fetched successfully'}, 200

    @jwt_required
    def delete(self, incident_id):
        ''' delete specific incident '''

        current_user = get_jwt_identity()

        incident = Incident().get_by_id(incident_id)

        if not incident:

            return {"Status": '404', "Message": "Incident does not exist"}, 404

        if current_user["username"] != incident.created_by:
            return {"message": "You can only deleted your own incident"}, 403

        if incident.status != 'draft':
            return {"message": f"you can only delete your incident if status is \'draft' your incident is {incident.status}"}

        incident.delete(incident_id)

        return {"Status": '200', "Message": "Incident deleted successfully"}, 200

    def patch(self, incident_id):
        ''' (PATCH) update specific incident '''

        data = PostIncidents.parser.parse_args()

        Type = data["Type"]
        location = data["location"]
        image = data["image"]
        video = data["video"]
        comment = data["comment"]

        incidents = Incident().get_by_id(incident_id)

        if incidents.status != "draft":
            return {"Status": '401', "Message": f"you status is {incidents.status} you can only edit an incident when status is \'draft' "}, 401

        incident = Incident(Type=Type, location=location,
                            image=image, video=video, comment=comment)

        incident.update(incident_id)
        return {"Status": '200', 'Data': f'{data}', "Message": "Incident updated successfully"}, 200

        return {"Status": '404', "Message": "Incident does not exist"}, 404
