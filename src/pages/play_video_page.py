import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = "Video is now playing."
  user_selection = displayOptions.display(
    [
<<<<<<< HEAD
      pages.START_PAGE
=======
      pages.LOGOUT_PAGE
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
