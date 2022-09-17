import json

database = {}

with open("users.json") as data_file:

  # database is a Python dictionary 
  database = json.load(data_file)
  
# Returns True if the list of users has less than 5 users
# Otherwise, return False -commented out for checking same username
# def can_add_more_users():
#   if (int(str(len(database["users"])))) < 5:
#     return True
#   else:
#     return False

def can_add_more_users():
  if len(database["users_list"]) < 5:
    return True

  else:
    return False

def user_exists_in_db(username, password):

    for user in database["users_list"]:
        if user["username"]  == username and user["password"] == password:
            return True
    
    return False


def add_user_to_db(username, password):

    new_user = {
      "username": username,
      "password": password
    }
  
    database["users_list"].append(new_user)

    # Updates the JSON file
    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent = 2)

