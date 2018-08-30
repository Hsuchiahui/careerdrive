#!/usr/bin/python3

import os

from flask import Flask
from flask import request
from flask import redirect
from flask import Response

from oauth2client.client import OAuth2WebServerFlow
from googleapiclient.discovery import build

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserRegisters.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserRegister(db.Model):
    __tablename__ = 'UserRegisters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=True)

flow = OAuth2WebServerFlow(client_id=os.environ['OAUTH_CLIENT_ID'],
        client_secret=os.environ['OAUTH_CLIENT_SECRET'],
        scope='https://www.googleapis.com/auth/userinfo.email',
        redirect_uri='https://careerdrive.herokuapp.com/oauth2callback')


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

