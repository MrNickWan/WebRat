from flask import Blueprint
from firebase_admin import db
from flask import request
from WebRat.util.rat_report import RatReportUtil


rat_report_blueprint = Blueprint('rat_report_service', __name__)


@rat_report_blueprint.route('/getReport', methods=['GET'])
def get_rat_report_data():
    ref = db.reference('/qa/ratData/31464015')
    print(ref.get())
    return 'works'


@rat_report_blueprint.route('/saveReport', methods=['post'])
def save_new_report_data():
    new_rat_report_data = request.get_json()
    rat_report_util = RatReportUtil()
    print(rat_report_util.submit_new_report(new_rat_report_data))

    return 'done'

