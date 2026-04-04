from models import db, FinancialRecord
from exceptions import ResourceNotFound
from models import User

# Creating arecord
def create_record(data,user_id):
    check_permission(user_id, "create")

    if not data.get("amount") or not data.get("type"):
        raise ValueError("Amount and Type are required")

    if data["type"] not in ["INCOME", "EXPENSE"]:
        raise ValueError("Type must be INCOME or EXPENSE")

    record = FinancialRecord(
        amount=data["amount"],
        type=data["type"],
        category=data.get("category"),
        date=data.get("date"),
        notes=data.get("notes")
    )

    db.session.add(record)
    db.session.commit()

    return record


# Get All records
def get_records():
    return FinancialRecord.query.all()


# Get by id
def get_record(record_id):
    record = FinancialRecord.query.get(record_id)

    if not record:
        raise ResourceNotFound("Record not found")

    return record


# Delete
def delete_record(record_id):
    record = get_record(record_id)

    db.session.delete(record)
    db.session.commit()


# Filter
def filter_records(type=None, category=None):
    query = FinancialRecord.query

    if type:
        query = query.filter_by(type=type)

    if category:
        query = query.filter_by(category=category)

    return query.all()


#Helper function to check permision
def check_permission(user_id, action):
    user = User.query.get(user_id)

    if not user:
        raise ResourceNotFound("User not found")

    if not user.active:
        raise ValueError("User is inactive")

    role = user.role

    if role == "VIEWER" and action != "read":
        raise ValueError("Viewer not allowed")

    if role == "ANALYST" and action in ["create", "update", "delete"]:
        raise ValueError("Analyst can only view")

    return user