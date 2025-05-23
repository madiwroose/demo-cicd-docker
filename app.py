from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from CI/CD Demo with GitHub Actions + Docker + K8s!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
