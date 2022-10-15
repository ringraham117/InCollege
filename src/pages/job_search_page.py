import src.constants.pages as pages
import src.shared.display_options as display_options
import src.router.router as router

def display_page():
    user_selection = display_options.display(
    [
      pages.JOB_POST_PAGE, 
      pages.ABOUT_PAGE, 
      pages.ACCESSIBILITY_PAGE,
      pages.USER_AGREEMENT_PAGE,
      pages.PRIVACY_POLICY_PAGE, 
      pages.COOKIE_POLICY_PAGE,
      pages.COPYRIGHT_POLICY_PAGE,
      pages.BRAND_POLICY_PAGE,
      pages.GUEST_CONTROLS_PAGE,
      pages.LANGUAGES_PAGE
    ])

    router.navigate_next_page(user_selection)   


def display_job_search_page():
    print("\nWhat do you want to do?\n")
    print("1. Post a job")
    print("2. Return to previous page\n")
    user_selection = input("Enter a selection: ")
    #navigate_user_to_requested_page(user_selection)


# def navigate_user_to_requested_page(user_selection):
#     if user_selection == "1":
#         job_post_page.display_job_post_page()
#     elif user_selection == "2":
#         state.goto_logged_in_state()
