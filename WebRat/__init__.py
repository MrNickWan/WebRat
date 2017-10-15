from flask import Flask
from WebRat.rat_report.routes import rat_report_blueprint

app = Flask(__name__)

app.register_blueprint(rat_report_blueprint, url_prefix='/rest/ratReport')


@app.route('/', methods=['GET'])
def root_handler():
    return 'hello from WebRat'


@app.route('/hello', methods=['GET'])
def handler():
    return 'aaaa'

