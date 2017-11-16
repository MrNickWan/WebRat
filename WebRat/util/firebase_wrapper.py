from firebase_admin import db


class FirebaseWrapper(object):
    def __init__(self):
        self.fb_db = db

    def save_data(self, loc, data):
        try:
            print('[FirebaseWrapper][save_data]: Saved at location ' + loc)
            self.fb_db.reference(loc).set(data)

            return True
        except:
            print('[FirebaseWrapper][save_data]: Saving failed at location ' + loc)
            return False

    def key_exist(self, loc, key):
        return self.fb_db.reference(loc).child(key).get() is not None

    def get_latest_entries(self, limit):
        return self.fb_db.reference('/pr/ratData/').order_by_key().limit_to_last(limit).get()

    def set_largest_unique_key(self, key):
        try:
            print('[FirebaseWrapper][set_key]: Key set ' + key)
            self.fb_db.reference('/pr/uniqueKey').set(key)

            return True
        except:
            print('[FirebaseWrapper][save_data]: Setting largest key failed')

            return False

    def get_largest_unique_key(self):
        result = self.fb_db.reference('/pr/ratData/').order_by_key().limit_to_last(1).get()

        return list(result.keys())[0]

if __name__ == '__main__':
    fb = FirebaseWrapper()
    fb.key_exist('/qa/ratData/', '1')


