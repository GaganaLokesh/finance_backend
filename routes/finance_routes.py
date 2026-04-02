from flask import Blueprint, request, jsonify
from services.finance_service import *

finance_routes = Blueprint('finance_routes', __name__)

#create record
@finance_routes.route('/records', methods=['POST'])
def add_record():
    data = request.get_json()

    record = create_record(data)

    return jsonify({
        "id": record.id,
        "amount": record.amount,
        "type": record.type,
        "category": record.category
    }), 201

#Get all records
@finance_routes.route('/records', methods=['GET'])
def get_all_records():
    records = get_records()

    result = []
    for r in records:
        result.append({
            "id": r.id,
            "amount": r.amount,
            "type": r.type,
            "category": r.category,
            "date": r.date
        })

    return jsonify(result)

#Filter records
@finance_routes.route('/records/filter', methods=['GET'])
def filter_api():
    type = request.args.get("type")
    category = request.args.get("category")

    records = filter_records(type, category)

    result = []
    for r in records:
        result.append({
            "id": r.id,
            "amount": r.amount,
            "type": r.type,
            "category": r.category
        })

    return jsonify(result)

#Deelete records

@finance_routes.route('/records/<int:id>', methods=['DELETE'])
def delete_api(id):
    delete_record(id)
    return {"message": "Deleted successfully"}