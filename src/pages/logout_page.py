from src.constants.student_success_story import STUDENT_SUCCESS_STORY 

import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
  page_description = STUDENT_SUCCESS_STORY
  user_selection = displayOptions.display(
    [
      pages.LOGIN_PAGE, 
      pages.SIGN_UP_PAGE, 
      pages.PLAY_VIDEO_PAGE, 
      pages.SEARCH_FOR_USERS_PAGE, 
      pages.USEFUL_LINKS_PAGE, 
      pages.IMPORTANT_LINKS_PAGE, 
      pages.EXIT_PAGE
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
