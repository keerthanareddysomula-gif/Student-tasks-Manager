from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Task Manager</h1>
    <p>Welcome! Your containerized application is running.</p>
    <p>Health check: <a href="/health">/health</a></p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
