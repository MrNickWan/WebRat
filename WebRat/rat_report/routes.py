from flask import Blueprint
from flask import request
from flask import jsonify
from WebRat.util.rat_report import RatReportUtil


rat_report_blueprint = Blueprint('rat_report_service', __name__)


@rat_report_blueprint.route('/getReport', methods=['GET'])
def get_rat_report_data():

    rt = RatReportUtil()
    result = rt.get_report_with_id(request.args.get('id'))

    return jsonify(result)


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

    return jsonify({
        'list': result
    })


@rat_report_blueprint.route('/setLargestUniqueKey', methods=['GET'])
def set_largest_unique_key():
    rt = RatReportUtil()
    result = rt.set_largest_unique_key(request.args.get('key'))

    return str(result)


@rat_report_blueprint.route('/getLargestUniqueKey', methods=['GET'])
def get_largest_unique_key():
    rt = RatReportUtil()
    result = rt.get_largest_unique_key()

    return str(result)


@rat_report_blueprint.route('/deleteReport', methods=['POST'])
def delete_report_handler():
    rt = RatReportUtil()

    return str(rt.delete_report(request.get_json()['reportId']))


@rat_report_blueprint.route('/getReportsInRange', methods=['GET'])
def get_reports_in_range():
    rt = RatReportUtil()

    return jsonify(rt.get_reports_in_range(request.args.get('begin'), request.args.get('end')))


@rat_report_blueprint.route('/getReportsInRangeGrouped', methods=['GET'])
def get_reports_in_range_grouped():
    rt = RatReportUtil()

    return jsonify(rt.get_reports_in_range_grouped(request.args.get('begin'), request.args.get('end')))


@rat_report_blueprint.route('/addOnlineUser', methods=['POST'])
def add_online_user():
    rt = RatReportUtil()

    return jsonify(rt.add_online_user(request.get_json()['user']))


@rat_report_blueprint.route('/removeOnlineUser', methods=['POST'])
def remove_online_user():
    rt = RatReportUtil()

    return jsonify(rt.remove_online_user(request.get_json()['user']))


@rat_report_blueprint.route('/isUserOnline', methods=['POST'])
def is_user_online():
    rt = RatReportUtil()

    return jsonify(rt.is_user_online(request.get_json()['user']))


@rat_report_blueprint.route('/whoIsOnline', methods=['GET'])
def who_is_online():
    rt = RatReportUtil()

    return jsonify(rt.who_is_online())



