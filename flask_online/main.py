from flask import Flask, request, json, jsonify
from flask.ext.cors import CORS
import hashlib, uuid

app = Flask(__name__)
app.debug = True

session_file = open('fixtures/sessions.tmp.json', 'r')
session_data = session_file.read()
if session_data == '':
    sessions = []
else:
    sessions = json.loads(session_data)
session_file.close()

CORS(app, resources=r'/*', headers='Content-Type')

def get_users():
    fixture_pointer = open('fixtures/users.json')
    return json.load(fixture_pointer)

def add_session(session):
    session_file = open('fixtures/sessions.tmp.json', 'w')
    sessions.append(session)
    session_file.write(json.dumps(sessions))
    session_file.flush()

@app.route("/")
def hello():
    return 'Hello World!'

@app.route('/session/create', methods=['POST'])
def session_create():
    data = request.json

    for user in get_users():
        if data['username'].lower() == user['username'].lower():
            if user['password'] == hashlib.md5(data['password']).hexdigest():
                # TODO: Persist session
                token = uuid.uuid4().hex
                session = {
                    "userId": user['id'],
                    "token": token
                }
                add_session(session)

                return jsonify(token=token)
    return '{"error":"Username or password invalid"}'

@app.route('/user', methods=['GET'])
def get_user():
    token = request.args['token']
    for session in sessions:
        if session['token'] == token:
            for user in get_users():
                if session['userId'] == user['id']:
                    return jsonify(user)

    return '{"error":"Session not found"}'

if __name__ == '__main__':
    app.run()
