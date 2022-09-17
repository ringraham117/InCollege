import database as db
import login
import menu


menu.print_login_menu()

user_input = input("\nEnter a selection: ")

if menu.user_chose_to_login(user_input):
  
    while True:
        print("\nLogin:")
        username = input("Username: ")
        password = input("Password: ")

        if db.user_exists_in_db(username, password):
            break

        else:
            print("Incorrect username/password, please try again.")

    print("\nYou have successfully logged in.")
    menu.print_top_level_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_find_job(user_input):
      print("Under construction.")

    elif menu.user_chose_to_find_someone(user_input):
      print("Under construction.")

    elif menu.user_chose_to_learn_a_skill(user_input):
      menu.print_skills_menu()
      user_input = input("Enter a selection: ")

      if user_chose_to_learn_web_dev():
        print("Under construction.")
      
      elif user_chose_to_learn_coding():
        print("Under construction.")
        
      elif user_chose_to_learn_communication():
        print("Under construction.")
      
      elif user_chose_to_learn_resume_critique():
        print("Under construction.")

      elif user_chose_to_learn_excel():
        print("Under construction.")

      elif user_chose_to_go_to_top_level_menu():
        pass


elif menu.user_chose_to_create_new_account(user_input):

    while True:

      print("\nCreate a new user:")
      username = input("Enter a username: ")
      password = input("Enter a password: ")
    
      if not db.can_add_more_users():
          print("All permitted accounts have been created, please come back later.")
          continue
  
      elif not login.username_is_unique(username):
          print("That username is not available.")
          continue
  
      elif login.password_is_too_short(password):
          print("Password is too short.")
          continue
  
      elif login.password_is_too_long(password):
          print("Password is too long.")
          continue
  
      elif not login.password_contains_uppercase_letter(password):
          print('Password must have at least one uppercase letter.')
          continue
  
      elif not login.password_contains_number(password):
          print("Password must have at least one numeral.")
          continue
  
      elif not login.password_contains_special_char(password):
          print("Password must have atleast one special character.")
          continue

      break

    db.add_user_to_db(username, password)
    print("Account successfully created.")