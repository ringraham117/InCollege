from logged_in_state import goto_logged_in_state

import database as db

def goto_logging_in_state():
  
  while True:
      print("\nLogin:")
      username = input("Username: ")
      password = input("Password: ")

      if db.user_exists_in_db(username, password):
            break

      else:
          print("Incorrect username/password, please try again.")

  print("\nYou have successfully logged in.")
  goto_logged_in_state()