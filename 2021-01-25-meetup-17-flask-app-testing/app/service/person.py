from app.model.person import Person
from app.db import db


class PersonService:

    def __init__(self):
        pass

    def create(self, name, primary_email):
        new_person = Person(name=name, primary_email=primary_email)
        db.session.add(new_person)
        db.session.commit()
        return True

    def retrieve(self):
        persons = Person.query.all()
        return persons

    def rerieve_one(self, id):
        person = Person.query.get_or_404(id)
        return person
