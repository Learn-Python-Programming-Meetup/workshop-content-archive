from app.model.person import Person
from app.db import db


class PersonService:

    def __init__(self, db_connection=None):
        if db_connection is not None:
            self.db = db_connection
        else:
            self.db = db

    def create(self, name, primary_email):
        new_person = Person(name=name, primary_email=primary_email)
        self.db.session.add(new_person)
        self.db.session.commit()
        return True

    def retrieve(self):
        persons = self.db.session.query(Person).all()
        return persons

    def retrieve_one(self, id):
        person = self.db.session.query(Person).filter_by(id=id).first()
        return person
