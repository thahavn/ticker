from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.json'

@app.route('/data.json', methods=['GET', 'PUT'])
def data():
    if request.method == 'GET':
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return jsonify(json.load(f))
        else:
            return jsonify([])
    elif request.method == 'PUT':
        headlines = request.get_json()
        if isinstance(headlines, list):
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(headlines, f, ensure_ascii=False, indent=2)
            return jsonify({"status": "ok"}), 200
        else:
            return jsonify({"error": "Invalid data format"}), 400

if __name__ == '__main__':
    app.run(port=8080)