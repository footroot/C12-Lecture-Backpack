from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define service URLs
USER_SERVICE_URL = "http://127.0.0.1:5001"
TASK_SERVICE_URL = "http://127.0.0.1:5002"

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    response = requests.post(f"{USER_SERVICE_URL}/users", json=data)
    return jsonify(response.json()), response.status_code

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    return jsonify(response.json()), response.status_code

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    response = requests.post(f"{TASK_SERVICE_URL}/tasks", json=data)
    return jsonify(response.json()), response.status_code

@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    response = requests.get(f"{TASK_SERVICE_URL}/tasks/{user_id}")
    return jsonify(response.json()), response.status_code

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    response = requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)  # Gateway runs on port 5000
