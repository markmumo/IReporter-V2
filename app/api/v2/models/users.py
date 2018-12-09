from datetime import datetime
from .database import Irepoterdb
from werkzeug.security import generate_password_hash, check_password_hash


class User(Irepoterdb):

    def __init__(self, firstname=None, lastname=None, othernames=None, email=None, password=None, phoneNumber=None, username=None, is_admin=False):
        super().__init__()

        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        self.phoneNumber = phoneNumber
        self.username = username
        self.is_admin = is_admin

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute(
            '''
            CREATE TABLE users(
                id serial PRIMARY KEY,
                firstname VARCHAR NOT NULL UNIQUE,
                lastname VARCHAR NOT NULL UNIQUE,
                othernames VARCHAR NOT NULL UNIQUE,
                email VARCHAR NOT NULL UNIQUE,
                password VARCHAR NOT NULL,
                phoneNumber INTEGER NOT NULL UNIQUE,
                username VARCHAR NOT NULL UNIQUE,
                is_admin BOOLEAN NOT NULL
            )
        '''
        )
        self.conn.commit()
        cur.close()

    def drop_table(self):
        cur = self.conn.cursor()
        cur.execute('DROP TABLE IF EXISTS users')
        self.conn.commit()
        cur.close()

    def add(self):
        '''add a user to user table'''
        cur = self.conn.cursor()
        cur.execute(
            '''INSERT INTO users(firstname, lastname, othernames, email, password, phoneNumber, username, is_admin) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''',
            (self.firstname, self.lastname, self.othernames, self.email,
             self.password, self.phoneNumber, self.username, self.is_admin)
        )

        self.conn.commit()
        cur.close()

    def serialize(self):
        return dict(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            othernames=self.othernames,
            email=self.email,
            password=self.password,
            phoneNumber=self.phoneNumber,
            username=self.username,
            is_admin=self.is_admin
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_user_by_id(self, id):
        '''get user by id'''
        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM users WHERE id=%s''',
                    (id, ))
        user = cur.fetchone()

        self.conn.commit()
        cur.close()

        if user:
            return self.objectify_user(user)
        return None

    # def get_user_by_id(self, Id):
    #     for user in Users:
    #         if user.id == Id:
    #             return user

    @staticmethod
    def get_user_by_username(username):
        for user in Users:
            if user.username == username:
                return user

    def get_user_by_email(self, email):
        for user in Users:
            if user.email == email:
                return user
            else:
                return {"Message": "user does not exist"}, 404

    def objectify_user(self, data):
        '''this converts a tuple into an object'''

        self.id = data[0]
        self.firstname = data[1]
        self.lastname = data[2]
        self.othernames = data[3]
        self.email = data[4]
        self.password = data[5]
        self.phoneNumber = data[6]
        self.username = data[7]
        self.is_admin = data[8]

        return self
