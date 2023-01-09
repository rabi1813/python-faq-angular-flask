from flask import Flask, redirect, url_for, request
from operations import get_data_type
from get_connection import db_connection
from flask_cors import CORS


connection = db_connection()

app = Flask(__name__)
CORS(app)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/data_type', methods=['POST', 'GET'])
def data_type():
    return get_data_type(connection)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
