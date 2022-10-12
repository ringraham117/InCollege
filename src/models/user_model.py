class User:

    def __init__(self, first_name, last_name, username, password, language = "English", sms = True, email = True, ads = True):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.language = language
        self.sms = sms
        self.email = email
        self.targeted_ads = ads
