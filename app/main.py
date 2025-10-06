from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict")
def predict():
    return jsonify({"result": 42}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
