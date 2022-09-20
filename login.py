# To do
# username_input = a string that user enters as their username to create a new account
# database = a Python dictionary
# Returns true if the username is not already in the JSON file
# Otherwise, return False
def username_is_unique(username_input, database):
  
  for user in database["users_list"]:
    if user["username"] in username_input:
      return False
      
  return True
  
def password_is_too_short(password):
  if len(password) < 8:
    return True

  else:
    return False

def password_is_too_long(password):
  if len(password) > 12:
    return True

  else:   
    return False

def password_contains_uppercase_letter(password):
  if any(char.isupper() for char in password):
    return True

  else:
    return False

def password_contains_number(password):
  if any(char.isdigit() for char in password):
    return True

  else:
    return False

def password_contains_special_char(password):
  valid_char = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
  
  if any(char in valid_char for char in password):
    return True

  else:
    return False
      
