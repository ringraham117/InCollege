import json

import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.authentication.auth as auth



def add_user(user):

  if (is_database_limit_reached()):
    notificationHandler.display_notification(
      errorMessages.USER_DATABASE_LIMIT_MESSAGE)
    return

  database = get_database_object()
  database["users"].append(user.__dict__)
  update_database_object(database)



def clear_users_list():
  database = {"users": []}

  # Opens the JSON file in write mode
  with open("databases/user_credentials.json", 'w') as data_file:
    json.dump(database, data_file, indent=2)



def is_database_limit_reached():
  database = get_database_object()
  return len(database["users"]) >= 10



def get_database_object():
  database_file = open('databases/user_credentials.json')
  file_data = database_file.read()
  return json.loads(file_data)



def get_user_by_id(unique_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == unique_id:
      return database_user
  return None


def get_user_by_username(username):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["username"] == username:
      return database_user
  return None



def update_database_object(updated_database):
  database_file = open('databases/user_credentials.json', 'w')
  json.dump(updated_database, database_file, indent=2)



def get_users_by_first_name(first_name):
  users = []
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["first_name"] == first_name:
      users.append(database_user)
  return users


def get_users_by_last_name(last_name):
  users = []
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["last_name"] == last_name:
      users.append(database_user)
  return users


def get_users_by_major(major):
  users = []
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["major"] == major:
      users.append(database_user)
  return users


def get_users_by_university(university):
  users = []
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["university"] == university:
      users.append(database_user)
  return users



def get_user_friend_requests(unique_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == unique_id:
      return database_user['friend_requests']
  return None



def send_friend_request(username):
  sender_id = auth.logged_in_user["unique_id"]
  receiver = get_user_by_username(username)
  if receiver is None:
    notificationHandler.display_notification(
      errorMessages.USER_NOT_FOUND_MESSAGE)
    return
  else:
    if (sender_id == receiver["unique_id"]):
      notificationHandler.display_notification(
        "Why are you trying to add yourself as a friend?")
      return
    receiver_id = receiver["unique_id"]
    database = get_database_object()
    for database_user in database["users"]:
      if database_user["unique_id"] == receiver_id:
        if sender_id in database_user["friend_requests"]:
          notificationHandler.display_notification(
            "Friend request already sent!")
        elif sender_id in database_user["friends"]:
          notificationHandler.display_notification(
            "You are already friends with this user!")
        else:
          database_user["friend_requests"].append(sender_id)
          notificationHandler.display_notification(
            "Friend request successfully sent!")
          update_database_object(database)


def add_user_to_friends(user_id, request_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == user_id:
      database_user["friends"].append(request_id)
  update_database_object(database)


def get_user_friends(unique_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == unique_id:
      return database_user['friends']
  return None

def delete_user_friend(user_id, friend_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == user_id:
      database_user["friends"].remove(friend_id)
  update_database_object(database)


def delete_user_friend_request(user_id, request_id):
  database = get_database_object()
  for database_user in database["users"]:
    if database_user["unique_id"] == user_id:
      database_user["friend_requests"].remove(request_id)
  update_database_object(database)


def set_user_language(unique_id, language):
  user = get_user_by_id(unique_id)
  if user is None:
    notificationHandler.display_notification(
      errorMessages.INVALID_USER_ID_MESSAGE)
    return
  else:
    user["language"] = language
    database = get_database_object()
    for database_user in database["users"]:
      if database_user["unique_id"] == unique_id:
        database_user["language"] = language
    update_database_object(database)


def set_user_sms(user_id, sms):
  database = get_database_object()
  for user in database["users"]:
    if user["unique_id"] == user_id:
      user["sms_notifications"] = sms
  update_database_object(database)


def set_user_ads(user_id, ads):
  database = get_database_object()
  for user in database["users"]:
    if user["unique_id"] == user_id:
      user["ad_notifications"] = ads
  update_database_object(database)

def set_user_email(user_id, email):
  database = get_database_object()
  for user in database["users"]:
    if user["unique_id"] == user_id:
      user["email_notifications"] = email
  update_database_object(database)


def get_user_by_first_last_name(first_name, last_name):
  database = get_database_object()
  for user in database["users"]:
    if user["first_name"] == first_name and user["last_name"] == last_name:
      return user
  return None


def set_user_title(username, title):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["title"] = title
  update_database_object(database)




def set_has_profile(username, has_profile):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["has_profile"] = has_profile
  update_database_object(database)


def set_user_about(username, about):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["about"] = about
  update_database_object(database)


def set_user_education(username, school, degree, years):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["school"] = school
      user["degree"] = degree
      user["years"] = years
  update_database_object(database)



def set_past_job_title(username, job_index, title):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["job_title"] = title

  update_database_object(database)


def set_user_major(username, major):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["major"] = major
  update_database_object(database)


def set_past_job_employer(username, job_index, employer):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["job_employer"] = employer

  update_database_object(database)
  
def set_past_job_start_date(username, job_index, start_date):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["start_date"] = start_date

  update_database_object(database)

def set_past_job_end_date(username, job_index, end_date):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["end_date"] = end_date

  update_database_object(database)

def set_past_job_location(username, job_index, location):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["location"] = location

  update_database_object(database)

def set_past_job_description(username, job_index, description):
  database = get_database_object()

  for user in database["users"]:
    if user["username"] == username:

      user_past_job_list = user["experience"]
      selected_job = user_past_job_list[job_index]
      selected_job["description"] = description

  update_database_object(database)

def set_user_university(username, university):
  database = get_database_object()
  for user in database["users"]:
    if user["username"] == username:
      user["university"] = university
  update_database_object(database)



  

