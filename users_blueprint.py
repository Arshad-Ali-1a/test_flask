from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

# Sample user database (would typically be a real database in a production app)
user_database = [
    {"id": 1, "username": "bookworm", "email": "bookworm@example.com", "purchases": []},
    {"id": 2, "username": "readaholic", "email": "readaholic@example.com", "purchases": []}
]

@users_bp.route('/')
def list_users():
    return jsonify([
        {"id": user['id'], "username": user['username'], "email": user['email']} 
        for user in user_database
    ])

@users_bp.route('/<int:user_id>')
def get_user(user_id):
    user = next((user for user in user_database if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@users_bp.route('/register', methods=['POST'])
def register_user():
    new_user = request.json
    new_user['id'] = len(user_database) + 1
    new_user['purchases'] = []
    user_database.append(new_user)
    return jsonify(new_user), 201