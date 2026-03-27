from flask import Blueprint, request, jsonify
from backend.model import User, db      # <-- changed
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = generate_password_hash(data['password'])

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User exists"}), 400

    new_user = User(username=username, password_hash=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
