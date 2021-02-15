from flask import request, jsonify
from flask import Blueprint, Response

from app.service.person import PersonService

person_bp = Blueprint('person', __name__)


@person_bp.route('/person/', methods=['POST'])
def create_person():
    person_service = PersonService()
    try:
        data = request.json
        name = data['name']
        primary_email = data['email']
        person_service.create(name=name, primary_email=primary_email)
        return Response("Accepted", status=202)
    except Exception as e:
        return Response(str(e), status=422)


@person_bp.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    person_service = PersonService()
    try:
        data = person_service.rerieve_one(id)
        result = {'name': data.name,
                  'primary email': data.primary_email}
        return jsonify(result)
    except Exception as e:
        return Response(str(e), status=422)


@person_bp.route('/person/', methods=['GET'])
def get_persons():
    person_service = PersonService()
    try:
        data = person_service.retrieve()
        result = formatter(data)
        return jsonify(result)
    except Exception as e:
        return Response(str(e), status=422)


@person_bp.errorhandler(404)
def api_not_found(e):
    return "Invalid API request"


def formatter(person):
    result = []
    for obj in person:
        result.append({
            'id': obj.id,
            'name': obj.name,
            'primary email': obj.primary_email
        })
    return result
