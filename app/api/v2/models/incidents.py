from datetime import datetime
from .database import Irepoterdb


class Incident(Irepoterdb):

    def __init__(self, created_by=None, Type=None, location=None, image=None, video=None, comment=None):
        super().__init__()
        self.created_on = datetime.now().replace(second=0, microsecond=0)
        self.created_by = created_by  # represents the user who created this record
        self.Type = Type
        self.location = location  # Lat Long coordinates
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
        '''add a user to user table'''
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

    def objectify_user(self, data):
        ''' maps user '''
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
