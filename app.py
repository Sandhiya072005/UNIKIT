from flask import Flask, jsonify, request, render_template
from ukit import chirp_common, directory  # Import necessary modules from chirp
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

# Example API endpoint to get radio features
@app.route('/api/radio/<radio_id>', methods=['GET'])
def get_radio_features(radio_id):
    try:
        radio_class = directory.get_radio(radio_id)
        features = radio_class.get_features()
        return jsonify(features.__dict__)
    except Exception as e:
        logging.error(f"Error fetching radio features: {e}")
        return jsonify({"error": str(e)}), 500

# Example API endpoint to set memory
@app.route('/api/radio/<radio_id>/memory', methods=['POST'])
def set_memory(radio_id):
    data = request.json
    try:
        radio_class = directory.get_radio(radio_id)
        memory = chirp_common.FrozenMemory(data)  # Assuming data is in the correct format
        radio_class.set_memory(memory)
        return jsonify({"message": "Memory set successfully!"}), 200
    except Exception as e:
        logging.error(f"Error setting memory: {e}")
        return jsonify({"error": str(e)}), 500

# Example API endpoint to get all available radios
@app.route('/api/radios', methods=['GET'])
def get_radios():
    try:
        radios = directory.get_radios()
        return jsonify([radio.__dict__ for radio in radios])
    except Exception as e:
        logging.error(f"Error fetching radios: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)