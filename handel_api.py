from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])

base_path = os.getcwd()
html_index_path = base_path + r"\vgsites_blogg\index.html"

@app.route("/", methods=["GET", "POST"])
def home():
    print(request.data)
    
    return jsonify({"data": "hello world"})

if __name__ == "__main__":
    app.run(debug=True)