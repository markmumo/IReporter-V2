from unittest import TestCase
from migrate import Tables
from app.api.v2.models.database import Irepoterdb
import json
from app import create_app


class BaseTest(TestCase):

    def setUp(self):
        ''' test setup'''

        app = create_app("testing")
        self.client = app.test_client()
        self.app_context = app.app_context()
        with self.app_context:
            Irepoterdb().init_app(app)
            Tables.drop(self)
            Tables.create(self)
            Tables.create_admin(self)

        self.create_incident = {
            "created_by": "mark",
            "Type": "redflag",
            "location": "j1.1018° S, 37.0144° juja",
            "status": "draft",
            "image": "corruption.png",
            "video": "corruption.mov",
            "comment": "very serious scandal"
        }

        self.edit_data = {
            "Type": "Intervention",
            "location": "Roysambu",
            "image": "betterpic.png",
            "video": "evenbettervid.mov",
            "comment": "corruption"
        }

        self.user_sign_up_data = {
            "firstname": "mark",
            "lastname": "mumo",
            "othernames": "sharkess",
            "email": "fake@gmail.com",
            "password": "markie1234",
            "phoneNumber": '0728124201',
            "username": "markie",
            "is_admin": "1"
        }

        self.user_sign_in_data = {
            "username": "markie",
            "password": "markie1234"
        }

        self.admin_sign_in_data = {
            "username": "adminirepoter",
            "password": "admin1234"
        }
        self.ghost_user_data = {
            "username": "ghostbusters",
            "password": "ghostbusters123"
        }

        self.invalid_password_data = {
            "username": "markie",
            "password": "markie%&\12345"
        }

        self.existing_user_name_data = {
            "username": "markie"
        }

        self.invalid_phone_number_data = {
            "firstname": "mark",
            "lastname": "mumo",
            "othernames": "sharkess",
            "email": "fake@gmail.com",
            "password": "fake1234",
            "phoneNumber": '072800000000000-420-121',
            "username": "markie",
            "is_admin": "1"
        }

        self.invalid_firstname_data = {
            "firstname": "###@@@###@@",
            "lastname": "mumo",
            "othernames": "sharkess",
            "email": "fake@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728-420-121',
            "username": "markie",
            "is_admin": "1"
        }

        self.invalid_lastname_data = {
            "firstname": "mark",
            "lastname": "###@@@###@@",
            "othernames": "sharkess",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728124201',
            "username": "markie",
            "is_admin": "1"
        }

        self.invalid_othernames_data = {
            "firstname": "mark",
            "lastname": "mumo",
            "othernames": "###@@@###@@",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728124201',
            "username": "markie",
            "is_admin": "1"
        }

        self.invalid_username_data = {
            "username": "###@@@###@@",
            "email": "fake@gmail.com",
            "password": "fake1234",
            "firstname": "mark",
            "lastname": "mumo",
            "othernames": "sharkess",
            "phoneNumber": '0728124201',
            "is_admin": "1"

        }
        self.email_exists_data = {
            "username": "markie",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "firstname": "mark",
            "lastname": "mumo",
            "othernames": "sharkess",
            "phoneNumber": '0728124201',
            "password": "shahkwss123",
            "is_admin": "1"
        }

    def post_incident(self):
        ''' create incident function '''

        token = self.get_jwt_token_as_user()

        response = self.client.post(
            "/api/v2/incident",
            data=json.dumps(self.create_incident),
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )

        return response

    def admin_sign_in(self):
        ''' admin sign_in function '''

        response = self.client.post(
            "api/v2/auth/Sign_in",
            data=json.dumps(self.admin_sign_in_data),
            headers={
                'content-type': 'application/json'
            }
        )
        return response

    def sign_up(self):
        ''' user sign_up function '''

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.user_sign_up_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def sign_in(self):
        ''' user sign_in function '''

        response = self.client.post(
            "api/v2/auth/Sign_in",
            data=json.dumps(self.user_sign_in_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def get_jwt_token_as_admin(self):
        """get jwt token """
        response = self.admin_sign_in()
        token = json.loads(response.data).get("token", None)
        return token

    def get_jwt_token_as_user(self):
        """get jwt token """
        self.sign_up()
        response = self.sign_in()
        token = json.loads(response.data).get("token", None)
        return token
