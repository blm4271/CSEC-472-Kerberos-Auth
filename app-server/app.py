from flask import *
import json
import sys

app = Flask(__name__)

def secretDecrypt(token, key):
    realKey = key * int(len(token) / len(key) + 1)
    realKey = realKey[:len(token)]

    return ''.join([chr(ord(x) ^ y) for x, y in zip(token, realKey)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appServer', methods=["POST"])
def appServer():
    token = request.get_json()
    sys.stderr.write("Client's Request: " + str(token) + '\n')

    if 'token' in token:
        token = token['token']
        token = secretDecrypt(token, b'@uth3nt!c@t!0n_L@b_5 _S3cr3t_K3y')
        token = json.loads(token)
        sys.stderr.write("Decrypted request from client: " + str(token) + '\n')
        
        if 'access_token' in token:
            return 'You may access the app server!'

        else:
            return 'You are denied access to the app server!'

    else:
        return 'No token, no app server!'

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)
