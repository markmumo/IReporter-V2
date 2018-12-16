from flask import Flask
from flask_restful import Resource, reqparse
import datetime
from flask_jwt_extended import create_access_token

from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from utils.validators import Validate


from werkzeug.security import check_password_hash


class Sign_in(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True,
                        help="This field can not be blank")
    parser.add_argument('password', type=str, required=True,
                        help="This field can not be blank")

    def post(self):
        data = Sign_in.parser.parse_args()
        username = data['username']
        password = data['password']

        user = User().get_user_by_username(username)

        if not user:
            return {'message': 'user not found'}, 404

        if not check_password_hash(user.password, password):
            return {'message': 'incorrect password'}, 401

        expires = datetime.timedelta(minutes=60)
        token = create_access_token(
            identity=user.serialize(), expires_delta=expires)
        return {'Status': '200', 'token': token, 'User': f'{username}', 'Message': 'successfully logged in'}, 200


class Sign_up(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('firstname', type=str, required=True)
    parser.add_argument('lastname', type=str, required=True)
    parser.add_argument('othernames', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('phoneNumber', type=str, required=True)
    parser.add_argument('username', type=str, required=True)

    def post(self):
        data = Sign_up.parser.parse_args()
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        password = data['password']
        phoneNumber = data['phoneNumber']
        username = data['username']

        if not Validate.validate_username(username):
            return {"Message": "username must be a string"}, 400
        if not Validate.validate_phone_number(phoneNumber):
            return {"Message": "please put a valid phone number"}, 400

        if not Validate.validate_email(email):
            return {"message": "Please enter valid email"}, 400

        if not Validate.validate_input_strings(firstname):
            return {"Message": "Please enter valid firstname"}, 400
        if not Validate.validate_input_strings(lastname):
            return {"Message": "Please enter valid lastname"}, 400
        if not Validate.validate_input_strings(othernames):
            return {"Message": "Please enter valid names"}, 400
        if not Validate.validate_password(password):
            return {"Message": "Password must be at least 8 characters"}, 400
        if User().get_user_by_email(email):
            return {"Message": f"{email} email address already taken,please try another"}, 400
        if User().get_user_by_username(username):
            return {"Message": f"{username} already taken, please try another"}, 400

        user = User(firstname, lastname, othernames, email, password,
                    phoneNumber, username)
        user.add()
        return {'Status': '201', 'User': f'{data}', 'Message': 'created successfully'}, 201

