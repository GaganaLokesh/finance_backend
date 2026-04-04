from flask import Blueprint, jsonify, request
from services.dashboard_services import get_summary
from services.finance_service import check_permission

dashboard_routes = Blueprint('dashboard_routes', __name__)


@dashboard_routes.route('/dashboard/summary', methods=['GET'])
def summary():
    user_id = request.args.get("user_id")

    # only read access needed
    check_permission(int(user_id), "read")

    data = get_summary()

    return jsonify(data)