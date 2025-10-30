import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = []
task_id_counter = 1

USER_SERVICE_URL = "http://127.0.0.1:5001"  # User Management Service URL

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'user_id' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    # Validate user ID by calling the User Management Service
    user_id = data['user_id']
    user_response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    if user_response.status_code != 200:
        return jsonify({'error': 'User not found'}), 404

    task_id = task_id_counter
    task = {'task_id': task_id, 'user_id': user_id, 'description': data['description']}
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    user_tasks = [task for task in tasks if task['user_id'] == user_id]
    return jsonify(user_tasks), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['task_id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(port=5002)  # Run the service on port 5002
