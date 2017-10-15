from flask import Blueprint

rat_report_blueprint = Blueprint('rat_report_service', __name__)


@rat_report_blueprint.route('/getReport', methods=['GET'])
def get_rat_report_data():
    return 'works'

