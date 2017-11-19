from WebRat.util.firebase_wrapper import FirebaseWrapper
import random
import datetime
import time

class RatReportUtil(object):
    def __init__(self):
        self.firebase = FirebaseWrapper()

    def submit_new_report(self, new_report):
        loc = '/pr/ratData/'
        new_unique_key = self.get_new_report_unique_key()

        if new_unique_key == '-1':
            print('[RatReportUtil][submit_new_report] getting new unique key failed')

            return False

        new_report['uniqueKey'] = new_unique_key
        new_report['createdDate'] = self.generate_timestamp()

        save_status = self.firebase.save_data(loc + new_unique_key, new_report)
        if save_status:
            if self.set_largest_unique_key(new_unique_key):
                return True

        return False

    def generate_report_keyat_loc(self, loc):
        candidate_key = random.randint(00000000, 99999999)
        taken = True
        while taken:
            if not self.get_content_with_loc_and_key(loc, str(candidate_key)):
                return str(candidate_key)

            candidate_key = random.randint(00000000, 99999999)

    def get_content_with_loc_and_key(self, loc, key):
        return self.firebase.key_exist(loc, key)

    def generate_timestamp(self):
        return '{:%m/%d/%Y %I:%M:%S %p}'.format(datetime.datetime.now())

    def get_latest_reports(self, limit=50):
        result_dict = self.firebase.get_latest_entries(limit)
        return [result_dict[k] for k in result_dict][::-1]

    def get_largest_unique_key(self):
        return self.firebase.get_largest_unique_key()

    def set_largest_unique_key(self, key):
        return self.firebase.set_largest_unique_key(key)

    def get_new_report_unique_key(self):
        curr_largest_uk = self.get_largest_unique_key()
        try:
            new_key = str(int(curr_largest_uk) + 1)
            return new_key
        except:
            return '-1'

    def get_report_with_id(self, report_id):

        result = {
            'status': True,
            'data': None
        }

        if report_id is None:
            result['status'] = False
            return result

        retrieve_result = self.firebase.get_report(report_id)

        if retrieve_result is None:
            result['status'] = False
            return result

        result['data'] = retrieve_result

        return result

    def delete_report(self, report_id):

        return self.firebase.delete_report(report_id)

    def get_reports_in_range(self, begin, end):

        return_result = {
            'status': False,
            'data': None
        }

        try:
            all_reports = self.firebase.get_all_reports()
            all_reports_list = [all_reports[k] for k in all_reports]

            begin_date = time.strptime(begin, '%m/%d/%Y')
            end_date = time.strptime(end, '%m/%d/%Y')
            result_list = []
            print('[Rat Report] filtering in progress')
            for report in all_reports_list:
                date_from_report = report['createdDate'].split(' ')[0]

                # if date_from_report.startswith('0'):
                    # date_from_report = date_from_report[1:]

                curr_date = time.strptime(date_from_report, '%m/%d/%Y')

                if begin_date <= curr_date <= end_date:
                    result_list.append(report)

            return_result['status'] = True
            return_result['data'] = result_list

            return return_result
        except Exception as e:
            print('Failed to do something: ' + str(e))
            return return_result


if __name__ == '__main__':
    test = RatReportUtil()
    test.generate_timestamp()
    # test.generate_report_keyat_loc('/qa/ratData')

