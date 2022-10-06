import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_discription = "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide."
  user_selection = displayOptions.display([], page_discription)
  router.navigate_next_page(user_selection)
