from backend.model import db
from backend.app import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized successfully!")
