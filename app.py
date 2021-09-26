import requests
from datetime import datetime
from flask import Flask, request, jsonify
from config import url, user_repo, pull, issue, fork, created_at, time_format

app = Flask(__name__)


@app.route('/get_repo', methods=['GET'])
def repo():
    response = requests.get(f'{url}{request.form.get(user_repo)}')
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code
    else:
        return jsonify(response.json())


@app.route('/get_pulls', methods=['GET'])
def pulls():

    response = requests.get(f'{url}{request.form.get(user_repo)}{pull}')
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code
    else:
        return jsonify(response.json())


@app.route('/get_unmerged_pulls', methods=['GET'])
def unmerged_pulls():
    response = requests.get(f'{url}{request.form.get(user_repo)}{pull}')
    response_dict = response.json()
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code
    else:
        check = []
        for item in response_dict:
            dict_date = datetime.strptime(item[created_at], time_format)
            mess_days = (datetime.now() - dict_date).days
            if mess_days >= 14:
                check.append(item)
        return jsonify(check), 200


@app.route('/get_issues', methods=['GET'])
def issues():
    response = requests.get(f'{url}{request.form.get(user_repo)}{issue}')
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code
    else:
        return jsonify(response.json())


@app.route('/get_forks', methods=['GET'])
def forks():
    response = requests.get(f'{url}{request.form.get(user_repo)}{fork}')
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code
    else:
        return jsonify(response.json())


if __name__ == '__main__':
    app.run()
