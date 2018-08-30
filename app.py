#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import redirect
from flask import Response

from oauth2client.client import OAuth2WebServerFlow
from googleapiclient.discovery import build

app = Flask(__name__)

flow = OAuth2WebServerFlow(client_id='',
        client_secret='',
        scope='https://www.googleapis.com/auth/userinfo.email',
        redirect_uri='')


@app.route('/', methods=['GET'])
def readfile_handler():
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)

@app.route('/oauth2callback')
def oauth_callback():
    auth_code = request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    service = build('oauth2', 'v2', credentials=credentials)
    return Response(service.userinfo().get().execute())

if __name__ == '__main__' :
    app.run(host = 'hmkrl.com', port = '8000', debug = False)
