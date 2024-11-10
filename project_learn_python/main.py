from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample data to send to the front end
    data = {"message": "Hello from the Python backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Adjust port as needed
