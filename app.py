from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier reçu'}), 400

    file = request.files['file']

    try:
        df = pd.read_csv(file)
        # Supposons que le CSV contient deux colonnes : "Nom" et "Valeur"
        data = df.to_dict(orient='records')
        return jsonify({'data': data}), 200
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la lecture du fichier : {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
