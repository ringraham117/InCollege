import json

  
# Returns True if the list of users has less than 5 users
# Otherwise, return False -commented out for checking same username
# def can_add_more_users():
#   if (int(str(len(database["users"])))) < 5:
#     return True
#   else:
#     return False

def get_database():
  with open("users.json") as data_file:
    database = json.load(data_file)
    return database

def can_add_more_users():
  with open("users.json") as data_file:
    database = json.load(data_file)
    
  return len(database["users_list"]) < 5
    
def user_exists_in_db(username, password):
    with open("users.json") as data_file:
      database = json.load(data_file)
      
    for user in database["users_list"]:
        if user["username"]  == username and user["password"] == password:
            return True
    
    return False


def add_user_to_db(username, password):
    with open("users.json") as data_file:
      database = json.load(data_file)
      
    new_user = {
      "username": username,
      "password": password
    }
  
    database["users_list"].append(new_user)

    # Updates the JSON file
    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent = 2)

