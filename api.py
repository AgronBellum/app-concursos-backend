# api.py
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/concursos", methods=["GET"])
def get_concursos():
    try:
        with open("concursos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
