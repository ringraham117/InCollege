# edit_experience_screen.py

import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

# A list of strings
screen_options = ["Job 1", "Job 2", "Job 3"]

# Global variable to store the index of the selected job (Set to None by default)
selected_job_index = None


def screen():
  screen_display = "Edit Experience Details"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  
  # Allow the user to select a job to edit
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):

  # Declares selected_job_index to refer to the global var so that we can change its value within the function
  global selected_job_index
  
  if (screen_exists(user_selection)):
    navigate_user(user_selection)

  elif user_selection == "Job 1":
    selected_job_index = 0

  elif user_selection == "Job 2":
    selected_job_index = 1

  elif user_selection == "Job 3":
    selected_job_index = 2
  
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    return screen()

  # Go to the edit job screen
  navigate_user(screenNames.EDIT_JOB_SCREEN)


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
