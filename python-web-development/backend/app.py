from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')

#Sample route
def home():
    return "Hello, Flask"

#Api endpoint example
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "This is your data"}
    return jsonify(data)           

# Post request example
@app.route('/api/post', methods=['POST'])
def post_data():
    input_data = request.json
    return jsonify({"received": input_data})



if __name__ == "__main__":
    app.run(debug=True)