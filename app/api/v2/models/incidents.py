from datetime import datetime
from distutils.util import execute

from .database import Irepoterdb


class Incident(Irepoterdb):

    def __init__(self, created_by=None, Type=None, location=None, image=None, video=None, comment=None):
        super().__init__()
        self.created_on = datetime.now().replace(second=0, microsecond=0)
        self.created_by = created_by
        self.Type = Type
        self.location = location
        self.status = "draft"
        self.image = image
        self.video = video
        self.comment = comment

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute(
            '''
            CREATE TABLE incidents(
                id serial PRIMARY KEY,
                created_on TIMESTAMP,
                created_by VARCHAR NOT NULL,
                Type VARCHAR NOT NULL,
                location VARCHAR NOT NULL,
                status VARCHAR NOT NULL,
                image VARCHAR NOT NULL,
                video VARCHAR NOT NULL,
                comment VARCHAR NOT NULL
            )
        '''
        )
        self.conn.commit()
        cur.close()

    def drop_table(self):
        cur = self.conn.cursor()
        cur.execute('DROP TABLE IF EXISTS incidents')
        self.conn.commit()
        cur.close()

    def add(self):
        '''add an incident to incident table'''
        cur = self.conn.cursor()
        cur.execute(
            '''INSERT INTO incidents(created_on, created_by, Type, location, status, image, video, comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''',
            (self.created_on, self.created_by, self.Type, self.location, self.status,
             self.image, self.video, self.comment)
        )

        self.conn.commit()
        cur.close()

    def serializer(self):
        return dict(
            id=self.id,
            created_on=str(self.created_on),
            created_by=self.created_by,
            Type=self.Type,
            location=self.location,
            status=self.status,
            image=self.image,
            video=self.video,
            comment=self.comment
        )

    def objectify_incident(self, data):
        ''' maps incident  '''
        self.id = data[0]
        self.created_on = data[1]
        self.created_by = data[2]
        self.Type = data[3]
        self.location = data[4]
        self.status = data[5]
        self.image = data[6]
        self.video = data[7]
        self.comment = data[8]

        return self

    def get_by_id(self, _id):
        ''' get incident by id '''
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM incidents WHERE id = %s", (_id, ))
        incident = cur.fetchone()

        cur.close()

        if incident:
            return self.objectify_incident(incident)
        return None

    def get_all_incidents(self):
        ''' get all incidents '''
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM incidents")
        incidents = cur.fetchall()
        cur.close()

        if incidents:
            return (self.objectify_incident(incident) for incident in incidents)
            return None

    def delete(self, incident_id):
        """ delete incident """
        cur = self.conn.cursor()
        cur.execute(
            "DELETE FROM incidents WHERE id = %s", (incident_id, ))
        self.conn.commit()
        cur.close()

    def update(self, incident_id):
        """ edit an incident """
        cur = self.conn.cursor()
        cur.execute(
            """ UPDATE incidents SET Type= %s, location= %s, image= %s, video= %s, comment= %s WHERE id = %s """, (
                self.Type, self.location, self.image, self.video, self.comment, incident_id)
        )
        self.conn.commit()
