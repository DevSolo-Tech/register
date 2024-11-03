# routes.py
from flask import Blueprint, request, jsonify
from models import db, User

# Create a Blueprint for your routes
api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Add user to the database
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(users_data), 200

@api.route('/')
def home():
    return "Welcome to the Registration API!"
