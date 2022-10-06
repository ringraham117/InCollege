import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router



def display_page():
  user_selection = displayOptions.display([pages.GENERAL_PAGE, pages.BROWSE_INCOLLEGE_PAGE, pages.BUSINESS_SOLUTIONS_PAGE, pages.DIRECTORIES_PAGE])
  router.navigate_next_page(user_selection)
  
  

