# Auth Server
# CSEC 472 - Lab 5
# Alex Rosse

from flask import *
import json
import requests
import hashlib
import sys
from cryptography.fernet import Fernet

app = Flask(__name__)
secret_key = b'@uth3nt!c@t!0n_L@b_5 _S3cr3t_K3y'

def encrypt(key,mess):
   f = Fernet(key)
   encrypted = f.encrypt(mess)
   return encrypted

@app.route('/')
def index():
    return 'Please Authenticate Yourself'

@app.route('/protected', methods=['POST'])
def protected():
   username = request.form['username']
   password = request.form['password']
   auth = requests.auth.HTTPBasicAuth(username,password)
   data = {'grant_type':'client-credentials'}
   req = requests.post('Insert Oauth Provider Here', data=data, auth=auth)
   if req.status_code == 400:
      return jsonify(auth='fail', token='')
   res = req.json()
   if 'access_token' in res:
      encryptToken = encrypt(secret_key, req.text)
      newRes = json.dumps({'auth':'sucess','token':encryptToken})
      passw = hashlib.sha256()
      passw.update(bytes(password, 'utf-8'))
      passKey = passw.digest()
      encryptPassw = encrypt(newRes, passKey)
      return jsonify(res=encryptPassw)
   else:
      return false

if __name__ == '__main__':
   app.run('0.0.0.0',port=80,debug=True)
