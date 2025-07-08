import os
import pandas as pd
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

RESULTS_FILE = "red_teaming_campaign_results.csv"

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/results')
def get_results():
    if not os.path.exists(RESULTS_FILE):
        return jsonify({"error": f"Results file '{RESULTS_FILE}' not found. Please run the orchestrator script first."}), 404
    try:
        df = pd.read_csv(RESULTS_FILE)
        results = df.to_dict(orient='records')
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": f"Failed to read or parse results CSV: {str(e)}"}), 500

if __name__ == '__main__':
    print(f"Serving frontend from: {os.path.join(os.getcwd(), app.static_folder)}")
    print(f"API endpoint for results: /api/results (reads from {RESULTS_FILE})")
    print("Access the dashboard at: http://127.0.0.1:5000/")
    app.run(debug=True)