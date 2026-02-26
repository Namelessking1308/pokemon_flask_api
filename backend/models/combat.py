from models import db
from datetime import datetime, timezone

class Combat(db.Model):
    __tablename__ = "combats"

    id = db.Column(db.Integer, primary_key=True)

    pokemon1_id = db.Column(
        db.Integer,
        db.ForeignKey("pokemons.id"),
        nullable=False
    )

    pokemon2_id = db.Column(
        db.Integer,
        db.ForeignKey("pokemons.id"),
        nullable=False
    )

    winner_id = db.Column(
        db.Integer,
        db.ForeignKey("pokemons.id"),
        nullable=False
    )

    turns = db.Column(db.Integer, nullable=False)
    battle_log = db.Column(db.JSON, nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )