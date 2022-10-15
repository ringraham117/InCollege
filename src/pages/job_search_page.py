import src.pages.job_post_page as job_post_page
import src.state as state

def display_page():
    pass

def display_job_search_page():
    print("\nWhat do you want to do?\n")
    print("1. Post a job")
    print("2. Return to previous page\n")
    user_selection = input("Enter a selection: ")
    navigate_user_to_requested_page(user_selection)


def navigate_user_to_requested_page(user_selection):
    if user_selection == "1":
        job_post_page.display_job_post_page()
    elif user_selection == "2":
        state.goto_logged_in_state()
