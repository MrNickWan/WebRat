from WebRat.util.firebase_wrapper import FirebaseWrapper


class RatReportUtil(object):
    def __init__(self):
        self.firebase = FirebaseWrapper()

    def submit_new_report(self, new_report):
        loc = '/qa/ratData/'
        return self.firebase.save_data(loc + str(new_report['uniqueKey']), new_report)


