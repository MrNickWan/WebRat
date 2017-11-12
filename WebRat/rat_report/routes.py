from flask import Blueprint
from firebase_admin import db
from flask import request
from flask import jsonify
from WebRat.util.rat_report import RatReportUtil


rat_report_blueprint = Blueprint('rat_report_service', __name__)


@rat_report_blueprint.route('/getReport', methods=['GET'])
def get_rat_report_data():
    ref = db.reference('/qa/ratData/31464015')
    print(ref.get())
    return 'works'


@rat_report_blueprint.route('/saveReport', methods=['post'])
def save_new_report_data():

    result = {
        'status': False,
        'info': ''
    }

    new_rat_report_data = request.get_json()
    print('New Report Data', new_rat_report_data)
    rat_report_util = RatReportUtil()

    if rat_report_util.submit_new_report(new_rat_report_data):
        result['status'] = True
        result['info'] = 'Saved'
    else:
        result['info'] = 'Check backend'

    return jsonify(result)


@rat_report_blueprint.route('/getContentWithUniqueKey', methods=['GET'])
def get_content_with_key():
    rt = RatReportUtil()
    result = rt.get_content_with_loc_and_key(request.args.get('loc'), request.args.get('key'))

    return str(result)


@rat_report_blueprint.route('/getLatest50', methods=['GET'])
def get_latest_50():
    rt = RatReportUtil()
    result = rt.get_latest_reports()

    return jsonify(result)
