from flask import Flask, request, json, jsonify
import hashlib, uuid

app = Flask(__name__)
app.debug = True

sessions = []

@app.route("/")
def hello():
    return 'Hello World!'

@app.route('/session/create', methods=['POST'])
def session_create():
    data = request.json
    fixture_pointer = open('fixtures/users.json')
    users = json.load(fixture_pointer)

    for user in users:
        if data['username'] == user['username']:
            if user['password'] == hashlib.md5(data['password']).hexdigest():
                # TODO: Persist session
                token = uuid.uuid4().hex
                session = {
                    "userId": user['id'],
                    "token": token
                }
                sessions.append(session)

                return jsonify(token=token)
            else:
                return '{"error":"Username or password invalid"}'

    return 'session'

if __name__ == '__main__':
    app.run()
