import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router

def display_page():
  user_selection = displayOptions.display([pages.SIGN_UP_PAGE, pages.ABOUT_PAGE, pages.PRESS_PAGE, pages.BLOG_PAGE, pages.CAREERS_PAGE, pages.DEVELOPERS_PAGE, pages.HELP_CENTER_PAGE])
  router.navigate_next_page(user_selection)
