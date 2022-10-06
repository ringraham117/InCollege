import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = "Top Level Menu\n------------"
  user_selection = displayOptions.display(
    [
      pages.JOB_SEARCH_PAGE, 
      pages.FIND_SOMEONE_YOU_KNOW_PAGE, 
      pages.LEARN_SKILLS_PAGE, 
      pages.START_PAGE, 
    ], 
    page_description)
  
  router.navigate_next_page(user_selection)
