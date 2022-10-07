from src.constants.student_success_story import STUDENT_SUCCESS_STORY 

import database as db
import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
   
    username = ""
    password = ""

    while True:
        print("\nLogin:")
        username = input("Username: ")
        password = input("Password: ")

        if db.user_exists_in_db(username, password):
            break

        else:
            print("Incorrect username/password, please try again.")


    print("\nYou have successfully logged in.")
    global loggedInUser
    loggedInUser = username
    router.navigate_next_page(pages.TOP_LEVEL_MENU_PAGE)
