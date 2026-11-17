from flask import Flask, jsonify, request
from generate_data import generate_synthetic_data

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/data")
def data():
    try:
        rows = int(request.args.get("rows", 1000))
        if rows <= 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Parameter 'rows' must be a positive integer"}), 400

    df = generate_synthetic_data(rows)
    records = df.to_dict(orient="records")
    return jsonify(records)

if __name__ == "__main__":
    import os
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug)
