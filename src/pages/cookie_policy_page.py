import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  cookies_policy = ''
  user_selection = displayOptions.display([], cookies_policy)
  router.navigate_next_page(user_selection)