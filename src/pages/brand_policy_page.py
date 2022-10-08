import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  brand_policy = ''
  user_selection = displayOptions.display([], brand_policy)
  router.navigate_next_page(user_selection)