from app import app
from models import db, Pokemon, Combat

with app.app_context():
    db.create_all()
    print("Tables créées/mises à jour !")