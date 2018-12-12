# module import
from flask_restful import Resource, reqparse

from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from utils.validators import Validate

from flask_jwt_extended import get_jwt_identity, jwt_required


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

        incident = Incident(
            created_by["username"], Type, location, image, video, comment)

        incident.add()

        return {"incident": "created successfully"}, 201


class AllIncidents(Resource):

    ''' GET all incidents '''

    def get(self):
        incidents = Incident().get_all_incidents()

        if not incidents:
            return {"message": "incidents not found"}, 404

        return {"incidents": [incident.serializer() for incident in incidents]}, 200


class Get_incident_by_id(Resource):

    ''' GET incident by id '''

    def get(self, incident_id):

        incident = Incident().get_by_id(incident_id)

        if not incident:

            return {"Message": "incident does not exit"}, 404

        else:

            return {"Incident": incident.serializer()}, 200

    def delete(self, incident_id):
        ''' delete specific incident '''

        incident = Incident().get_by_id(incident_id)

        if not incident:

            return {"message": "incident does not exist"}, 404

        else:

            incident.delete(incident_id)

            return {"Message": "Incident deleted successfully"}, 200

    def put(self, incident_id):
        ''' (PUT) update specific incident '''

        data = PostIncidents.parser.parse_args()

        Type = data["Type"]
        location = data["location"]
        image = data["image"]
        video = data["video"]
        comment = data["comment"]

        incidents = Incident().get_by_id(incident_id)

        if incidents.status != "draft":
            return {"message": f"you status is {incidents.status} you can only edit an incident when status is \'draft' "}, 401

        incident = Incident(Type=Type, location=location,
                            image=image, video=video, comment=comment)

        incident.update(incident_id)
        return {"message": "incident updated successfully"}, 200

        return {"message": "incident does not exist"}, 404
