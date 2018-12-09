import json

from app.tests.v1.base_test import BaseTest


class TestIncident(BaseTest):

    def test_post_incident(self):

        response = self.post_incident()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "incident"], "created successfully")

        """Test get incident"""

    def test_get_incidents(self):
        response = self.client.get("/api/v1/incident")
        self.assertEqual(response.status_code, 200)

        """Test get incident by id"""

    def test_get_incident_by_id(self):

        self.post_incident()

        response = self.client.get(
            "/api/v1/incident/3",
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)

        """Test to delete an incident"""

    def test_delete_incident_by_id(self):

        self.post_incident()
        response = self.client.delete(
            "/api/v1/incident/1",
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)

        """Test to  update specific incident"""

    def test_patch(self):

        res = self.post_incident()
        response = self.client.patch(
            "/api/v1/incident/3",
            data=json.dumps(self.create_incident),
            headers={
                'content-type': 'application/json'
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_username(self):
        """ Test if username is invalid """

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.invalid_username_data),
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(json.loads(response.data)[
                         "Message"], "username can only contain alphanumeric characters only and a minimum of 4 characters")
        self.assertEqual(response.status_code, 400)

    def test_email_exists(self):
        '''test for signup with an existing email address'''

        self.signup()

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.email_exists),
            headers={'content-type': 'application/json'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "email adress already taken")

    def test_validate_firstname(self):
        '''test for a valid firstname'''

        self.signup()

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.invalid_firstname),
            headers={"content-type": "application/json"}
        )
        print(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid firstname")

    def test_validate_phone_number(self):
        '''test for a valid phone number'''

        self.signup()

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.invalid_phone_number),
            headers={"content-type": "application/json"}
        )
        print(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "please put valid phone number")

    def test_validate_lastname(self):
        '''test for a valid lastname'''

        self.signup()

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.invalid_lastname),
            headers={"content-type": "application/json"}

        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid lastname")

    def test_validate_othernames(self):
        '''test for valid othernames'''

        self.signup()

        response = self.client.post(
            "api/v1/auth/Sign_up",
            data=json.dumps(self.invalid_othernames),
            headers={"content-type": "application/json"}

        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid names")

    def test_signup(self):
        '''test for signing up'''
