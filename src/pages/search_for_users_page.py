import database as db
import src.constants.pages as pages
import src.router.router as router


def display_page():
    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    if db.name_found_in_db(first_name, last_name):
        print("\nThey are a part of the InCollege system.")
        router.navigate_next_page(pages.ASK_TO_JOIN_PAGE)

    else:
        print("\nThey are not yet a part of the InCollege system.")
        router.navigate_next_page(pages.LOGOUT_PAGE)
