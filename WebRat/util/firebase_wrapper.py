from firebase_admin import db


class FirebaseWrapper(object):
    def __init__(self):
        self.fb_db = db

    def save_data(self, loc, data):
        try:
            self.fb_db.reference(loc).set(data)
            return True
        except:
            print('[FirebaseWrapper][save_data]: Saving failed at location ' + loc)
            return False

