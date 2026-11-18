
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "application": "application-paas",
        "framework": "Flask"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
