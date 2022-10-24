# edit_job_screen.py

import src.authentication.auth as auth
import src.routing.router as router
import src.constants.error_messages as errorMessages
import src.constants.screen_names as screenNames
import src.screens.logged_in.edit_experience_screen as editExperienceScreen
import src.services.user_controller as userController
import src.shared.screen_display_handler as displayHandler
import src.shared.notification_handler as notificationHandler

# A list of strings
# Past jobs have a title, employer, date started, date ended, location, description
screen_options = [ "Edit Job Title", "Edit Employer", "Edit Start Date", "Edit End Date", "Edit Location", "Edit Description"
]


def screen():
  screen_display = "Edit Job Details"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):  
  
  # Stores the username of the logged in user
  logged_in_username = auth.logged_in_user['username']
  
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  
  elif user_selection == "Edit Job Title":
    title = input("\nEnter title: ")
    userController.set_past_job_title(logged_in_username, editExperienceScreen.selected_job_index, title)

  elif user_selection == "Edit Employer":
    employer = input("\nEnter employer: ")
    userController.set_past_job_employer(logged_in_username, editExperienceScreen.selected_job_index, employer)

  elif user_selection == "Edit Start Date":
    start_date = input("\nEnter start date: ")
    userController.set_past_job_start_date(logged_in_username, editExperienceScreen.selected_job_index, start_date)

  elif user_selection == "Edit End Date":
    end_date = input("\nEnter end date: ")
    userController.set_past_job_end_date(logged_in_username, editExperienceScreen.selected_job_index, end_date)

  elif user_selection == "Edit Location":
    location = input("\nEnter location: ")
    userController.set_past_job_location(logged_in_username, editExperienceScreen.selected_job_index, location)

  elif user_selection == "Edit Description":
    description = input("\nEnter description: ")
    userController.set_past_job_description(logged_in_username, editExperienceScreen.selected_job_index, description)
  
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
