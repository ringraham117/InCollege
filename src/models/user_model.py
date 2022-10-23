import src.models.user_settings_model as userSettingsModel
import src.models.profile_model as profileModel


class User:

    def __init__(self,
                 user_id="",
                 username="",
                 password="",
                 active_profile=False,
                 profile=profileModel.Profile(),
                 settings=userSettingsModel.Settings()):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.profile = profile
        self.active_profile = active_profile
        self.settings = settings
        self.jobPosts = []
        self.friends = []
        self.friend_requests = []
