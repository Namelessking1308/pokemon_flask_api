from models import db

class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sprite_url = db.Column(db.String(255))

    combats_as_p1 = db.relationship(
        "Combat",
        foreign_keys="Combat.pokemon1_id",
        backref="pokemon1_ref",
        lazy=True
    )
    combats_as_p2 = db.relationship(
        "Combat",
        foreign_keys="Combat.pokemon2_id",
        backref="pokemon2_ref",
        lazy=True
    )
    combats_won = db.relationship(
        "Combat",
        foreign_keys="Combat.winner_id",
        backref="winner_ref",
        lazy=True
    )