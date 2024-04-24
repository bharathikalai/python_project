from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/api/example', methods=['GET'])
def get_example_data():
    data = {'message': 'Hello,World!'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
