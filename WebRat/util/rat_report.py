from WebRat.util.firebase_wrapper import FirebaseWrapper
import random
import datetime

class RatReportUtil(object):
    def __init__(self):
        self.firebase = FirebaseWrapper()

    def submit_new_report(self, new_report):
        loc = '/qa/ratData/'
        unique_key = self.generate_report_keyat_loc(loc)
        new_report['unique_key'] = unique_key
        new_report['createdDate'] = self.generate_timestamp()

        return self.firebase.save_data(loc + unique_key, new_report)

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
        return self.firebase.get_latest_entries(limit)

if __name__ == '__main__':
    test = RatReportUtil()
    test.generate_timestamp()
    # test.generate_report_keyat_loc('/qa/ratData')

