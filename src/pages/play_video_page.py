import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = "Video is now playing."
  user_selection = displayOptions.display(
    [
      pages.LOGOUT_PAGE
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
