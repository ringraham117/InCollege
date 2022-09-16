import json

database = {}

with open("users.json") as data_file:

  # database is a Python dictionary 
  database = json.load(data_file)

  # Temporary
  print( "Length of the user list: " + str( len(database["users"]) ) )
  print( "Data type of database[\"users\"]: " + str( type(database["users"]) ) )
  
# Returns True if the list of users has less than 5 users
# Otherwise, return False -commented out for checking same username
def can_add_more_users():
  if (int(str(len(database["users"])))) < 5:
    return True
  else:
    return False
  
def user_exists_in_db(username_input, password_input):

    for user in database["users"]:
        if user["username"]  == username_input and user["password"] == password_input:
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

