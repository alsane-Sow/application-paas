
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Mon application PaaS</title>
    </head>
    <body>
        <h1>Bienvenue sur mon application Cloud !</h1>
        <p>Cette application utilise Python et Flask.</p>
        <p>Elle est hébergée sur une plateforme PaaS.</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "application": "application-paas"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
