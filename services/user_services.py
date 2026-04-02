from models import db, User, FinancialRecord
from exceptions import ResourceNotFound

def validate_role(role):
    valid_roles = ["VIEWER", "ANALYST", "ADMIN"]

    if role not in valid_roles:
        raise ValueError("Invalid role")

# USER SERVICES

def create_user(data):

    if not data.get("name") or not data.get("email") or not data.get("role"):
        raise ValueError("Missing required fields")

    validate_role(data["role"]) 

    user = User(
        name=data["name"],
        email=data["email"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():
    return User.query.all()


def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ResourceNotFound("User not found")
    return user

def update_user(user_id, data):
    user = User.query.get(user_id)

    if not user:
        raise ResourceNotFound("User not found")

    if "name" in data:
        user.name = data["name"]

    if "email" in data:
        user.email = data["email"]

    if "role" in data:
        validate_role(data["role"])
        user.role = data["role"]

    db.session.commit()

    return user

def toggle_user_status(user_id):
    user = User.query.get(user_id)

    if not user:
        raise ResourceNotFound("User not found")

    user.active = not user.active
    db.session.commit()

    return user