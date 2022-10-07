import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = "\nJoin your friends on the InCollege system!"
  user_selection = displayOptions.display(
    [
      pages.LOGIN_PAGE,
      pages.SIGN_UP_PAGE,
      pages.START_PAGE
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
