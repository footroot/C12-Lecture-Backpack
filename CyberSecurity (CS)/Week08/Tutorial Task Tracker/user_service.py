from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}
user_id_counter = 1

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    user_id = user_id_counter
    users[user_id] = {'name': data['name'], 'email': data['email']}
    user_id_counter += 1
    return jsonify({'user_id': user_id, 'name': data['name'], 'email': data['email']}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user_id': user_id, **user}), 200

if __name__ == '__main__':
    app.run(port=5001)  # Run the service on port 5001
