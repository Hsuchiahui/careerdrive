from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

# views
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def add_record():
    req_data = request.form
    username = req_data['username']
    password = req_data['password']
    # record = Record(name = name, cost = cost)
    # db.session.add(record)
    # db.session.commit()
    return 'User ' + username + ' login with password ' + password, 200

if __name__ == '__main__' :
    app.run(host = 'localhost', port = '5000', debug = False)
