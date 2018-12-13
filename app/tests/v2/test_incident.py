import json

from app.tests.v2.base_test import BaseTest


class TestIncident(BaseTest):
    def test_get_jwt_token(self):
        ''' Test get jwt token '''

        self.sign_up()
        response = self.sign_in()

        self.assertEqual(response.status_code, 200)

        self.assertIn("token", json.loads(response.data))

    def test_admin_sign_in(self):
        ''' test admin successful sign_in '''
        response = self.admin_sign_in()

        self.assertEqual(response.status_code, 200)

    def test_sign_up(self):
        ''' test successful sign_up '''
        response = self.sign_up()
        self.assertEqual(response.status_code, 201)

    def test_sign_in(self):
        ''' test successful sign_in '''
        self.sign_up()
        response = self.sign_in()
        self.assertEqual(response.status_code, 200)

    def test_ghost_user_sign_in(self):
        ''' Test if a user does not exist '''
        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_in",
            data=json.dumps(self.ghost_user_data),
            headers={'content-type': 'application/json'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 404)

        self.assertEqual(json.loads(response.data)[
                         "message"], "user not found")

    def test_post_incident(self):

        token = self.get_jwt_token_as_user()

        data = {
            "location": "jkuat"
        }
        self.post_incident()

        response = self.client.post(
            "/api/v2/models/Incidents/1/incidents",
            data=json.dumps(data),
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )
        return response

    def test_get_incidents(self):
        '''Test get incident'''
        self.post_incident()
        response = self.client.get("/api/v2/incident")
        self.assertEqual(response.status_code, 200)

    def test_get_incident_by_id(self):
        '''Test get incident by id'''
        token = self.get_jwt_token_as_user()

        self.post_incident()

        response = self.client.post(
            "/api/v2/Incidents/1/incidents",
            data=json.dumps(self.create_incident),
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )
        response = self.client.get(
            "api/v2/incident/1",
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_incident_by_id(self):
        '''Test to delete an incident'''

        token = self.get_jwt_token_as_user()

        self.post_incident()

        response = self.client.delete(
            "/api/v2/incident/1",
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 200)

    def test_edit_incident(self):
        '''Test to edit a specific incident'''

        token = self.get_jwt_token_as_user()

        self.post_incident()

        response = self.client.put(
            "/api/v2/incident/1",
            data=json.dumps(self.edit_data),
            headers={'content-type': 'application/json',
                     'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_username(self):
        ''' Test if username is invalid '''

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_username_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(json.loads(response.data)[
                         "Message"], "username can only contain alphanumeric characters only and a minimum of 4 characters")
        self.assertEqual(response.status_code, 400)

    def test_existing_username(self):
        ''' Test if username is existing '''
        self.sign_up()
        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.existing_user_name_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

    def test_email_exists(self):
        '''test for sign_up with an existing email address'''

        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.email_exists_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_password(self):
        ''' Test invalid password '''
        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_password_data),
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, 400)

    def test_validate_firstname(self):
        '''test for a valid firstname'''

        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_firstname_data),
            headers={"content-type": "application/json"}
        )
        print(response.data)
        self.assertEqual(response.status_code, 400)

    def test_validate_phone_number(self):
        '''test for a valid phone number'''

        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_phone_number_data),
            headers={"content-type": "application/json"}
        )
        print(response.data)
        self.assertEqual(response.status_code, 400)

    def test_validate_lastname(self):
        '''test for a valid lastname'''

        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_lastname_data),
            headers={"content-type": "application/json"}

        )

        self.assertEqual(response.status_code, 400)

    def test_validate_othernames(self):
        '''test for valid othernames'''

        self.sign_up()

        response = self.client.post(
            "api/v2/auth/Sign_up",
            data=json.dumps(self.invalid_othernames_data),
            headers={"content-type": "application/json"}

        )

        self.assertEqual(response.status_code, 400)
