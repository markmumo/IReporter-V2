import psycopg2
from flask import current_app


class Irepoterdb:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                current_app.config.get('DATABASE_URL'))

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def init_app(self, app):
        self.conn = psycopg2.connect(app.config.get('DATABASE_URL'))
