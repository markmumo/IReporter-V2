from datetime import datetime
from .database import Irepoterdb


class Incident(Irepoterdb):

    def __init__(self, created_by=None, Type=None, location=None, status=None, image=None, video=None, comment=None):
        super().__init__()
        self.created_on = datetime.now().replace(second=0, microsecond=0)
        self.created_by = created_by  # represents the user who created this record
        self.Type = Type  # [red-flag, intervention]
        self.location = location  # Lat Long coordinates

        # [draft, under investigation, resolved, rejected]
        self.status = status
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
                created_by VARCHAR NOT NULL UNIQUE,
                lastname VARCHAR NOT NULL UNIQUE,
                Type VARCHAR NOT NULL UNIQUE,
                location VARCHAR NOT NULL UNIQUE,
                status VARCHAR NOT NULL,
                image INTEGER NOT NULL UNIQUE,
                video VARCHAR NOT NULL UNIQUE,
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

    # def get_incident_by_id(self, id):
    #     for incident in incidents:
    #         if incident.id == id:
    #             return incident
