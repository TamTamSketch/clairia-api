from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Traitement factice pour démonstration
    return jsonify({"message": f"Fichier '{file.filename}' reçu avec succès."})

@app.route("/")
def home():
    return "API Clairia opérationnelle 🚀"
