# edit_education_screen.py

import src.authentication.auth as auth
import src.constants.error_messages as errorMessages
import src.constants.screen_names as screenNames
import src.routing.router as router
import src.services.user_controller as userController
import src.shared.format_input_first_upper as formatToFirstUpper
import src.shared.screen_display_handler as displayHandler
import src.shared.notification_handler as notificationHandler



# A list of strings
# Education part of each profile includes school name, degree, & years attended
#screen_options = [ "Edit school name", "Edit degree", "Edit year school started", "Edit year school ended"
#]
# This option CANNOT be "Edit Education"
screen_options = ["Edit Education Details"]


def screen():
  screen_display = "Edit Education"
  user_selection = displayHandler.display_controller( screen_options, 
                                                     screen_display)
  handle_user_selection(user_selection)

def get_user_education():
  print("\nEnter your education")
  school = input("\n\t\tEnter school: ")
  degree = input("\n\t\tEnter degree: ")
  years = input("\n\t\tEnter years: ")

  spaced_pascal_case_school = formatToFirstUpper.format_input_first_upper(school)
  spaced_pascal_case_degree = formatToFirstUpper.format_input_first_upper(degree)
  
  return spaced_pascal_case_school, spaced_pascal_case_degree, years

def handle_user_selection(user_selection):
  
  # If the screen name is in the list of valid screens
  if (screen_exists(user_selection)):
    
    # Go to that screen
    navigate_user(user_selection)
  elif user_selection in screen_options:
    if user_selection == "Edit Education Details":
      username = auth.logged_in_user['username']
      school, degree, years = get_user_education()
      userController.set_user_education(username, school, degree, years)
        

  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens

