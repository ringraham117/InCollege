import json
import src.models.user_model as user_model

def get_database():
  with open("databases/user_credentials.json") as data_file:
    database = json.load(data_file)
    return database

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
  database = get_database()
      
  for user in database["users_list"]:
      if user["first_name"]  == first_name and user["last_name"] == last_name:
          return True
  
  return False
