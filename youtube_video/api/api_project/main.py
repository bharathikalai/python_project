from flask import Flask,jsonify,request

apps = Flask(__name__)

tasks = []


@apps.route('/api/tasks',methods=['Get'])
def get_tasks():
    return jsonify({'tasks':tasks})


@apps.route('/api/tasks',methods=['POST'])
def create_task():
    data = request.json
    tasks.append(data)
    return jsonify({'message': 'Task created successfully'})


if __name__ == "__main__":
    apps.run(debug=True)