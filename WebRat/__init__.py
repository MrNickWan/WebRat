from flask import Flask
from WebRat.rat_report.routes import rat_report_blueprint
import firebase_admin
from firebase_admin import credentials
import os

app = Flask(__name__, static_url_path='', static_folder='static')
app.register_blueprint(rat_report_blueprint, url_prefix='/rest/ratReport')

firebase_admin.initialize_app(credentials.Certificate(os.path.dirname(__file__) + '/key.json'), {
    'databaseURL': 'https://ratdatabase2340.firebaseio.com'
})


@app.route('/', methods=['GET'])
def root_handler():
    print('[Backend] hitting default handler')
    return app.send_static_file('index.html')


@app.route('/signIn', methods=['GET'])
def sign_in_handler():
    return app.send_static_file('index.html')


@app.route('/newReport', methods=['GET'])
def new_report_handler():
    return app.send_static_file('index.html')


@app.route('/hello', methods=['GET'])
def handler():
    return 'aaaa'


@app.route('/viewLatestReports', methods=['GET'])
def view_latest_reports_handler():
    return app.send_static_file('index.html')


@app.route('/viewReport', methods=['GET'])
def view_report_handler():
    return app.send_static_file('index.html')


# @app.route("/", defaults={"path": ""})
# @app.route("/<string:path>")
# @app.route("/<path:path>")
# def catch_all(path):
#     return 'You want path: %s' % path


