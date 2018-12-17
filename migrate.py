import os

from flask.cli import with_appcontext

from app.api.v2.models.incidents import Incident
from app.api.v2.models.users import User
from run import app


class Tables:
    def create(self):
        User().create_table_users()
        Incident().create_table_incidents()

    def drop(self):
        User().drop_table_users()
        Incident().drop_table_incidents()

    def create_admin(self):
        admin = User(firstname='Admin', lastname='irepoter', othernames='name', email='admin@gmail.com',
                     password='admin1234', phoneNumber='12345678', username='adminirepoter', is_admin=True)
        admin.add()


if __name__ == '__main__':
    with app.app_context():
        Tables().drop()
        Tables().create()
        Tables().create_admin()
