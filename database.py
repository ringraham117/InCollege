import json
import src.models.user_model as user_model

def get_user_by_username(username):
    users_list = get_users_list()

    for user in users_list:
      if user["username"] == username:
        return user

def get_users_by_last_name(last_name):
  users_list = get_users_list()
  output_list = []

  for user in users_list:
    if user["last_name"] == last_name:
      output_list.append(user)

  return output_list

def get_users_list():
    with open("databases/user_credentials.json") as data_file:
        database = json.load(data_file)
        return database["users_list"]


def can_add_more_users():
    with open("databases/user_credentials.json") as data_file:
        database = json.load(data_file)

    return len(database["users_list"]) < 10


def user_exists_in_db(username, password):
    with open("databases/user_credentials.json") as data_file:
        database = json.load(data_file)

    for user in database["users_list"]:
        if user["username"] == username and user["password"] == password:
            return True

    return False


def add_user_to_db(first_name, last_name, university, major, username, password):
    with open("databases/user_credentials.json") as data_file:
        database = json.load(data_file)

    new_user = user_model.User(first_name, last_name, university, major, username, password)

    database["users_list"].append(new_user.__dict__)

    # Updates the JSON file
    with open("databases/user_credentials.json", "w") as myFile:
        json.dump(database, myFile, indent=2)


def name_found_in_db(first_name, last_name):
    users_list = get_users_list()

    for user in users_list:
        if user["first_name"] == first_name and user["last_name"] == last_name:
            return True

    return False

def last_name_found_in_db(last_name):
    users_list = get_users_list()

    for user in users_list:
        if user["last_name"] == last_name:
            return True

    return False

def univ_found_in_db(university):
    users_list = get_users_list()

    for user in users_list:
        if user["university"] == university:
            return True

    return False

def major_found_in_db(major):
    users_list = get_users_list()

    for user in users_list:
        if user["major"] == major:
            return True

    return False

def clear_users_list():
    database = {"users_list": []}

    # Opens the JSON file in write mode
    with open("databases/user_credentials.json", 'w') as data_file:
        json.dump(database, data_file, indent=2)


# This one
def clear_jobs_list():
    empty_jobs_list = {"jobs": []}

    # Opens the JSON file in write mode
    with open("databases/job_posting.json", 'w') as data_file:
        json.dump(empty_jobs_list, data_file, indent=2)


def get_jobs_list():
    with open("databases/job_posting.json") as data_file:
        database = json.load(data_file)
        return database["jobs"]


def job_exists_in_db(title, description, employer, location, salary):
    for job in get_jobs_list():
        if job["title"] == title \
        and job["descriptionage"] == description \
        and job["employer"] == employer \
        and job["location"] == location \
        and job["salary"] == salary:

            return True

    return False


def get_jobs_dictionary():
    with open("databases/job_posting.json") as data_file:
        dictionary = json.load(data_file)

    return dictionary

def get_guest_controls(username):
  with open("databases/user_credentials.json") as users_file:
    dictionary = json.load(users_file)
    for user in dictionary['users_list']:
      if (user['username'] == username):
        return {
          'sms': user['sms'], 
          'email': user['email'], 
          'targeted_ads': user['targeted_ads']
        }

def write_guest_controls(username, controls):
    with open("databases/user_credentials.json") as users_file:
      dictionary = json.load(users_file)
    for user in dictionary['users_list']:
      if (user['username'] == username):
        user['sms'] = controls['sms']
        user['email'] = controls['email']
        user['targeted_ads'] = controls['targeted_ads']
    with open("databases/user_credentials.json", 'w') as user_file:
      json.dump(dictionary, user_file, indent = 2)

def get_db_as_dictionary():
  with open("databases/user_credentials.json") as data_file:
    database = json.load(data_file)
    return database

def update_users_list(users_list):
  
  # Opens the JSON file in write mode
  with open("databases/user_credentials.json", 'w') as data_file:
    
    # Updates the JSON file
    json.dump(users_list, data_file, indent=2)

#def list_matches(last_name, university, major):
def list_matches(last_name):
    #open list of users
    users_list = get_users_list()

    #if user's last name is in list, display user info
    for user in users_list:
        #if user["last_name"] == last_name or user["university"] == university or user["major"] == major:
      if user["last_name"] == last_name:
            first = user["first_name"]
            last = user["last_name"]
            uni = user["university"]
            major = user["major"]
            id = user["id"]
            #I need to format this output
            print("Name:", first, last,"       University:", uni,"       Major:", major,"      User ID:", id)
          
        #else: print("user does not match")


# Bilal coded
def get_id(username):
  user_list = get_users_list()
  for user in user_list:
    if user['username'] == username:
      return user['id']

def get_user_by_id(id):
  user_list = get_users_list()
  for user in user_list:
    if user['id'] == id:
      return user

def get_friends_list(id):
  user = get_user_by_id(id)
  return user['friends']

def get_friend_requests(id):
  user = get_user_by_id(id)
  return user['friend_requests']

def is_friend(user_id, friend_id):
  user = get_user_by_id(user_id)
  if friend_id in user['friends']:
    return True
  else:
    return False

def request_friend(user_id, friend_id):
  # user = get_user_by_id(user_id)
  # user['friend_requests'].append(friend_id)
  if is_friend(user_id, friend_id):
    return False
  dictionary = get_db_as_dictionary()
  for user in dictionary['user_list']:
    if user['id'] == user_id:
      user['friend_requests'].append(friend_id)      
  with open('databases/user_credentials.json', 'w') as user_file:
    json.dump(dictionary, user_file, indent=2)
  return True

def add_friend(user_id, friend_id):
  if is_friend(user_id, friend_id): 
    return False
  
  # user = get_user_by_id(user_id)
  # friend = get_user_by_id(friend_id)
  # user['friends'].append(friend_id)
  # friend['friends'].append(user_id)

  dictionary = get_db_as_dictionary()
  for user in dictionary['user_list']:
    if user['id'] == user_id:
      user['friends'].append(friend_id)
    elif user['id'] == friend_id:
      user['friends'].append(user_id)
      
  with open('databases/user_credentials.json', 'w') as user_file:
    json.dump(dictionary, user_file, indent=2)
    
  return True

def remove_friend(user_id, friend_id):
  if not is_friend(user_id, friend_id):
    return False

  dictionary = get_db_as_dictionary()
  for user in dictionary['user_list']:
    if user['id'] == user_id:
      user['friends'].remove(friend_id)
    elif user['id'] == friend_id:
      user['friends'].remove(user_id)
      
  with open('databases/user_credentials.json', 'w') as user_file:
    json.dump(dictionary, user_file, indent=2)
    
  return True