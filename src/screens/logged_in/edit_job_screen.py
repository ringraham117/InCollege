# edit_job_screen.py

import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

# A list of strings
# Past jobs have a title, employer, date started, date ended, location, description
screen_options = [ "Edit title", "Edit employer", "Edit start date", "Edit end date", "Edit location", "Edit description"
]


def screen():
  screen_display = "Edit Job Details"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
