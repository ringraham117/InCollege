import json
import src.models.user_model as user_model

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

def clear_db():
    database = {"users_list": []}
  
    # Opens the JSON file in write mode
    with open("databases/user_credentials.json", 'w') as data_file:
        json.dump(database, data_file, indent=2)
