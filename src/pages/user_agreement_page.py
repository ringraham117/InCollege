import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  user_agreement = ''
  user_selection = displayOptions.display([], user_agreement)
  router.navigate_next_page(user_selection)