from flask import Blueprint, request, jsonify
from services.user_services import create_user, get_all_users, get_user,update_user,toggle_user_status

routes = Blueprint('routes', __name__)


@routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    user = create_user(data)

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }), 201


@routes.route('/users', methods=['GET'])
def fetch_users():
    users = get_all_users()

    result = []
    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role
        })

    return jsonify(result)


@routes.route('/users/<int:user_id>', methods=['GET'])
def fetch_user(user_id):
    user = get_user(user_id)

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    })

@routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user_api(user_id):
    data = request.get_json()

    user = update_user(user_id, data)

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    })

@routes.route('/users/<int:user_id>/status', methods=['PATCH'])
def change_status(user_id):
    user = toggle_user_status(user_id)

    return jsonify({
        "id": user.id,
        "active": user.active
    })