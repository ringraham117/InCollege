import json
import src.models.user_model as user_model
import state

def get_users_list():
    with open("databases/user_credentials.json") as data_file:
        database = json.load(data_file)
        return database["users_list"]

def can_add_more_users():
  with open("databases/user_credentials.json") as data_file:
    database = json.load(data_file)
    
  return len(database["users_list"]) < 5
    
def user_exists_in_db(username, password):
    with open("databases/user_credentials.json") as data_file:
      database = json.load(data_file)
      
    for user in database["users_list"]:
        if user["username"]  == username and user["password"] == password:
            return True
    
    return False


def add_user_to_db(first_name, last_name, username, password):
  with open("databases/user_credentials.json") as data_file:
      database = json.load(data_file)

  new_user = user_model.User(first_name, last_name, username, password)

  database["users_list"].append(new_user.__dict__)

  # Updates the JSON file
  with open("databases/user_credentials.json", "w") as myFile:
      json.dump(database, myFile, indent=2)


def name_found_in_db(first_name, last_name):      
  for user in get_users_list():
      if user["first_name"]  == first_name and user["last_name"] == last_name:
          return True
  
  return False

def clear_users_list():
    database = {"users_list": []}
  
    # Opens the JSON file in write mode
    with open("databases/user_credentials.json", 'w') as data_file:
        json.dump(database, data_file, indent=2)

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
  