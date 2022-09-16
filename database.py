import json

database = {}

with open("users.json") as data_file:

    database = json.load(data_file)

# To do
# Returns True if the JSON file has less than 5 users
# Otherwise, return False
def can_add_more_users():
    return True
  
def user_exists_in_db(username_input, password_input):

    for user in database["users"]:
        if username_input == user["username"] and password_input == user["password"]:
            return True
    
    return False


def add_user(username_input, password_input):

    new_user = {
      "username": username_input,
      "password": password_input
    }
  
    database["users"].append(new_user)

    # Updates the JSON file
    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent = 2)

