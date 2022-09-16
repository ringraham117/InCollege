import database as db
import menu_module

def create_new_user():
  while True:

        username = input("Enter a username: ")
        password = input("Enter a password: ")

        # Cannot add more users
        if not db.can_add_more_users():

            print(
                "All permitted accounts have been created, please come back later."
            )
            continue

        # Username is not unique
        elif not username_is_unique(username):

            print("That username is not available.")
            continue

        # password is not valid
        elif not password_is_valid(password):
          print("The password must be between 8 and 12 characters. Also, it must contain at least one capital letter, one digit, and one special character"
            )
          continue

        db.add_user(username, password)
        print("Account successfully created.")
        break


# To do
# Returns true if the username is not already in the JSON file
# Otherwise, return False
def username_is_unique(user_input):
    return True


# To do
# Returns true if the password is 8-12 characters, has a capital letter, has a digit, and had a special character
# Otherwise, return False
def password_is_valid(password_input):
  valid_char = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    
  if len(password_input) <= 8:
      print("Password is too short.")
  elif len(password_input) > 12:
    print("Password is too long.")
  elif not any(char.isupper() for char in password_input):
    print('Password must have at least one uppercase letter.')
  elif not any(char in valid_char for char in password_input):
      print("Password must have atleast one special character.")
  elif not any(char.isdigit() for char in password_input):
    print("Password must have atleast one numeral.")
  else:
    print("Password has been created successfully!")
  
# Returns True if the password contains a special character
# Returns False if the password does not contain a special character
def password_contains_special_char(password_input):

  special_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}

  for char in password_input:
    if char in special_chars:
      return True

  return False

def login():

    while True:
        username = input("\nUsername: ")
        password = input("Password: ")

        if db.user_exists_in_db(username, password):
            break

        print("Incorrect username/password, please try again")

    print("You have successfully logged in.")
    menu_module.print_top_level_menu()
    user_input = input("Enter a selection: ")

    if user_input == "1":
        print("Under construction")

    elif user_input == "2":
        print("Under construction")

    elif user_input == "3":
        menu_module.print_skills_menu()
