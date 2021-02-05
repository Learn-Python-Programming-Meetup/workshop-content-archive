from app.db import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    primary_email = db.Column(db.String(200), nullable=False)
