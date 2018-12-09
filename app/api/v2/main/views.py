# module import
from flask_restful import Resource, reqparse

from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from utils.validators import Validate


class PostIncidents(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("created_by", type=str, required=True)
    parser.add_argument("Type", type=str, required=True)
    parser.add_argument("location", type=str, required=True)
    parser.add_argument("status", type=str, required=True)
    parser.add_argument("image", type=str, required=True)
    parser.add_argument("video", type=str, required=True)
    parser.add_argument("comment", type=str, required=True)

    def post(self):

        data = PostIncidents.parser.parse_args()

        created_by = data["created_by"]
        Type = data["Type"]
        location = data["location"]
        status = data["status"]
        image = data["image"]
        video = data["video"]
        comment = data["comment"]

        if not Validate.is_string(created_by):

            return {"message": "must be a string"}, 400

        if not Validate.is_string(Type):
            return {"type": "must be a string"}, 400

        incident = Incident(created_by, Type, location,
                            status, comment, image, video)

        incidents.append(incident)

        return {"incident": "created successfully"}, 201


class AllIncidents(Resource):

    """ GET all incident """

    def get(self):

        return {"Incidents": [Incident.serializer() for Incident in incidents]}, 200


class Get_incident_by_id(Resource):

    """ GET incident by id """

    def get(self, id):

        incident = Incident().get_incident_by_id(id)

        if not incident:

            return {"Message": "incident does not exit"}, 404

        else:

            return {"Incident": incident.serializer()}, 200

    def delete(self, id):
        """" DELETE specific incident """

        delete_incident = Incident().get_incident_by_id(id)
        if not delete_incident:

            return {"message": "incident does not exist"}, 404

        else:

            incidents.remove(delete_incident)

            return {"Message": "Incident deleted successfully"}, 200

    def patch(self, id):
        """ (PATCH) update specific incident """

        data = PostIncidents.parser.parse_args()

        created_by = data['created_by']
        Type = data['Type']
        location = data['location']
        status = data['status']
        image = data['image']
        video = data['video']
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
            specific_incident.video = video
            specific_incident.comment = comment

            return {"Incident": specific_incident.serializer()}, 200
