from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_handler():
    return 'hello from WebRat'


@app.route('/hello', methods=['GET'])
def handler():
    return 'aaaa'

