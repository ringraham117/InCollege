import src.models.job_model as jobModel

class User:

  def __init__(self,
               unique_id="",
               username="",
               password="",
               first_name="",
               last_name="",
               university="",
               major="",
               has_profile=False,
               title="",
               about="",            
               school="",
               degree="",
               years="",
               education="",
               language="English",
               sms_notifications=True,
               email_notifications=True,
               ad_notifications=True):
    self.username = username
    self.unique_id = unique_id
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.language = language
    self.sms_notifications = sms_notifications
    self.email_notifications = email_notifications
    self.ad_notifications = ad_notifications
    self.friends = []
    self.friend_requests = []
    self.has_profile = has_profile
    self.title = title
    self.university = university
    self.major = major
    self.about = about
    self.profile =  ""
    self.experience = [
      {},
      {},
      {}
    ]
     

    
  

