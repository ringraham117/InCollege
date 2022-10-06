import src.shared.display_options as displayOptions
import src.router.router as router
from src.constants.student_success_story import STUDENT_SUCCESS_STORY 

def display_page():
  page_description = STUDENT_SUCCESS_STORY
  user_selection = displayOptions.display(
    [
      "Login", 
      "Sign Up", 
      "Play video (\"Why Join InCollege?\")", 
      "Search for InCollege users", 
      "Useful Links", 
      "InCollege Important Links", 
      "Exit"], 
    page_description)
  
  router.navigate_next_page(user_selection)
