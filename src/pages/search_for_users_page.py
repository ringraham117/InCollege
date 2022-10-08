import database as db
import src.constants.pages as pages
<<<<<<< HEAD
=======
import src.shared.display_options as displayOptions
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
import src.router.router as router


def display_page():
    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    if db.name_found_in_db(first_name, last_name):
        print("\nThey are a part of the InCollege system.")
        router.navigate_next_page(pages.ASK_TO_JOIN_PAGE)
<<<<<<< HEAD

=======
    
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
    else:
        print("\nThey are not yet a part of the InCollege system.")
        router.navigate_next_page(pages.LOGOUT_PAGE)
