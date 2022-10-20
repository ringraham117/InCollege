import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController


##MAY NEED TO PUT MORE SCREEN OPTIONS 
screen_options = []

def screen():
  screen_display = "Profile Information For " + auth.logged_in_user[
    "username"] + "!" "\n"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display,
                                                     previousScreen=False)
  handle_user_selection(user_selection)
  
## Should this remain here
def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()

## DISPLAY USER INFO - DOUBLE CHECK
def display_profile_information():
  user_id = auth.logged_in_user['unique_id']
  user = userController.get_user_by_id(user_id)
  print("Username: " + user['username'],
                  "FirstName: " + user['first_name'],
                  "LastName: " + user['last_name'],
                  "University: " + user['university'],
                  "Major: " + user['major'],
                  sep=" ")

def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens