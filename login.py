# To do
# username_input = a string that user enters as their username to create a new account
# database = a Python dictionary
# Returns true if the username is not already in the JSON file
# Otherwise, return False
def username_is_unique(username_input, users_list):
  
  for user in users_list:
    if user["username"] == username_input:
      return False
      
  return True
  
def password_is_too_short(password):
  return len(password) < 8    

def password_is_too_long(password):
  return len(password) > 12
    
def password_contains_uppercase_letter(password):
  return any(char.isupper() for char in password)
    
def password_contains_number(password):
  return any(char.isdigit() for char in password)
    
def password_contains_special_char(password):
  valid_char = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
  
  return any(char in valid_char for char in password)
    
