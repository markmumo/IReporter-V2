from app.api.v2.auth.views import All_users, Get_user_by_id, Get_users_by_email
from app.api.v2.auth.views import Sign_in, Sign_up
from app.api.v2.main.views import PostIncidents, AllIncidents, Get_incident_by_id


def url(api):
    api.add_resource(PostIncidents, "/incident")
    '''GET all incidents'''
    api.add_resource(AllIncidents, "/incident")

    '''GET incident by id'''
    api.add_resource(Get_incident_by_id, "/incident/<int:incident_id>")

    '''SignUp'''
    api.add_resource(Sign_up, '/auth/Sign_up')

    '''SignIn'''
    api.add_resource(Sign_in, '/auth/Sign_in')

    '''GET all Users'''
    api.add_resource(All_users, '/users')
    api.add_resource(Get_user_by_id, '/users/<int:id>')
    api.add_resource(Get_users_by_email, '/users/<string:email>')

    return None
