import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = "We are here to help!"
  user_selection = displayOptions.display([], page_description)
  router.navigate_next_page(user_selection)
