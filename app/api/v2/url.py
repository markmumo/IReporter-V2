from flask_restful import Api
from app.api.v2.admin.views import Admin_Get_incident_by_id, Incidents
from app.api.v2.auth.views import Sign_in, Sign_up
from app.api.v2.main.views import AllIncidents, Get_incident_by_id, \
    PostIncidents


def url(api):


    api.add_resource(PostIncidents, "/incident")
    '''GET all incidents'''
    api.add_resource(AllIncidents, "/incident")
    api.add_resource(Incidents, "/all/incidents")

    '''GET incident by id'''
    api.add_resource(Get_incident_by_id, "/incident/<int:incident_id>")
    api.add_resource(Admin_Get_incident_by_id, "/admin/incident/<int:id>")

    '''SignUp'''
    api.add_resource(Sign_up, '/auth/Sign_up')

    '''SignIn'''
    api.add_resource(Sign_in, '/auth/Sign_in')

    return None
