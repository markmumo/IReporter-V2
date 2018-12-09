from unittest import TestCase
import json
from app import create_app


class BaseTest(TestCase):

    def setUp(self):
        app = create_app("testing")
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.app_context.pop()

        self.create_incident = {
            "created_by": "mark",
            "Type": "redflag",
            "location": "j1.1018° S, 37.0144° juja",
            "status": "draft",
            "image": "corruption.png",
            "video": "corruption.webm",
            "comment": "very serious scandal"
        }

        self.user_signup_data = {
            "firstname": "markie",
            "lastname": "fhfjkdhfef",
            "othernames": "sharkess",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728-124-201',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_phone_number = {
            "firstname": "markie",
            "lastname": "fhfjkdhfef",
            "othernames": "shkaesdf",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '072800000000000-420-121',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_firstname = {
            "firstname": "#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
            "lastname": "fhfjkdhfef",
            "othernames": "shaksefs",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728-420-121',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_lastname = {
            "firstname": "marekk",
            "lastname": "#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
            "othernames": "sghesajks",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728-420-121',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_othernames = {
            "firstname": "marekk",
            "lastname": "mummoo",
            "othernames": "#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "phoneNumber": '0728-420-121',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_password = {
            "firstname": "marekk",
            "lastname": "mummoo",
            "othernames": "markss",
            "email": "fakessssss@gmail.com",
            "password": "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "phoneNumber": '0728-420-121',
            "username": "mark",
            "is_admin": "1"
        }

        self.invalid_username_data = {
            "username": "@@@@@@@@@@@@",
            "email": "fakes@gmail.com",
            "password": "fake1234",
            "firstname": "markie",
            "lastname": "fhfjkdhfef",
            "othernames": "shgakedyds",
            "phoneNumber": '0728-420-121',
            "is_admin": "1"

        }
        self.email_exists = {
            "username": "markie",
            "email": "fake@gmail.com",
            "password": "fake1234",
            "firstname": "markie",
            "lastname": "fhfjkdhfef",
            "othernames": "shdtjaks",
            "phoneNumber": '0728-420-121',
            "password": "shahkwss123",
            "is_admin": "1"

        }

    def post_incident(self):
        response = self.client.post(
            "/api/v1/incident",
            data=json.dumps(self.create_incident),
            headers={'content-type': 'application/json'}
        )

        return response

    def signup(self):
        """ user signup function """
        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.user_signup_data),
            headers={'content-type': 'application/json'}
        )
        return response
