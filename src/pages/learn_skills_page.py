

import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = ''
  user_selection = displayOptions.display(
    [
      pages.WEB_DEVELOPMENT_PAGE, 
      pages.CODING_PAGE, 
      pages.COMMUNICATION_PAGE, 
      pages.RESUME_CRITIQUE_PAGE, 
      pages.MICROSOFT_EXCEL_PAGE 
      
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
