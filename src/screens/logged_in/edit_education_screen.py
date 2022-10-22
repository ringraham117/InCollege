# edit_education_screen.py

import src.authentication.auth as auth
import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.screens.logged_in.create_profile_screen as createProfile

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

def handle_user_selection(user_selection):
  
  # If the screen name is in the list of valid screens
  if (screen_exists(user_selection)):
    
    # Go to that screen
    navigate_user(user_selection)
  elif user_selection in screen_options:
    if user_selection == "Edit Education Details":
      username = auth.logged_in_user['username']
      school, degree, years = createProfile.get_user_education()
      userController.set_user_education(username, school, degree, years)
        

  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens










  ##The details school name, degree, year started, & year ended are yet to be defined
  # in the user_controller.py
  # elif user_selection == "Edit school name":
  #   school_name = input("\nEnter school name: ")
  #   userController.set_user_school_name(username, school_name)

  # elif user_selection == "Edit degree":
  #   school_degree = input("\nEnter degree: ")
  #   userController.set_user_school_degree(username, school_degree)
  
  # elif user_selection == "Edit year school started":
  #   year_school_started = input("\nEnter year school started: ")
  #   userController.set_user_year_school_started(username, year_school_started)

  # elif user_selection == "Edit year school ended":
  #   year_school_ended = input("\nEnter year school ended: ")
  #   userController.set_user_year_school_ended(username, year_school_ended)
    