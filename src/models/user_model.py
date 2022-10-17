class User:

    def __init__(self,
                 unique_id="",
                 username="",
                 password="",
                 first_name="",
                 last_name="",
                 university="",
                 major="",
                 language="English",              
                 sms_notifications=True,
                 email_notifications=True,
                 ad_notifications=True):
        self.unique_id = unique_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.language = language
        self.university = university
        self.major = major
        self.sms_notifications = sms_notifications
        self.email_notifications = email_notifications
        self.ad_notifications = ad_notifications
        self.friends = []
        self.friend_requests = []
