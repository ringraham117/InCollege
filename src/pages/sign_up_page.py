<<<<<<< HEAD
import database as db
import login
import src.constants.pages as pages
=======
from src.constants.student_success_story import STUDENT_SUCCESS_STORY 

import database as db
import login
import src.constants.pages as pages
import src.shared.display_options as displayOptions
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
import src.router.router as router


def display_page():
<<<<<<< HEAD

=======
  
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
    print("\nCreate a new user:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not db.can_add_more_users():
        print("All permitted accounts have been created, please come back later.")

    elif not login.username_is_unique(username, db.get_users_list()):
        print("That username is not available.")

    elif login.password_is_too_short(password):
        print("Password is too short.")

    elif login.password_is_too_long(password):
        print("Password is too long.")

    elif not login.password_contains_uppercase_letter(password):
        print('Password must have at least one uppercase letter.')

    elif not login.password_contains_number(password):
        print("Password must have at least one numeral.")
<<<<<<< HEAD

    elif not login.password_contains_special_char(password):
        print("Password must have atleast one special character.")

    else:
        db.add_user_to_db(first_name, last_name, username, password)
        print("Account successfully created.")

    router.navigate_next_page(pages.START_PAGE)
=======
    
    elif not login.password_contains_special_char(password):
        print("Password must have atleast one special character.")
    
    else:
        db.add_user_to_db(first_name, last_name, username, password)
        print("Account successfully created.")
    
    router.navigate_next_page(pages.LOGOUT_PAGE)
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
