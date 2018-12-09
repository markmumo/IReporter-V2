import os

from app import create_app
from app.api.v1.models import incidents


app = create_app(os.getenv("FLASK_CONFIG") or "development")
