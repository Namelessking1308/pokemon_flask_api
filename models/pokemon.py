from models import db

class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    hp = db.Column(db.Integer, nullable = False)
    attack = db.Column(db.Integer, nullable = False)
    defense = db.Column(db.Integer, nullable = False)
    sprite_url = db.Column(db.String(255))