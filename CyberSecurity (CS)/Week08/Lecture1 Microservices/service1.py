from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the Miroservice!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)