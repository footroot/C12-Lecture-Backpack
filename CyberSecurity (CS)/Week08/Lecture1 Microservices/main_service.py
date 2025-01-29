from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/api/aggregate', methods=['GET'])
def aggregate_data():
    try:
        response = requests.get('http://localhost:5000/api/data')
        data = response.json()
    except Exception:
        data = {}

    return jsonify({'message': 'Aggregated data', 'data': data})


if __name__ == "__main__":
    app.run(debug=True, port=5001)