import src.authentication.auth as auth
import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.models.user_profile_model as profileModel
import src.services.profile_controller as profileController

screen_options = ["Create Profile"]


def screen():
  screen_display = "Create/View Your Profile"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  elif user_selection in screen_options:
    if user_selection == "Create Profile":
      profile = get_user_profile_data()
      profileController.add_profile(profile)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
  screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens


def get_user_profile_data():
  user = auth.logged_in_user['username']
  title = input("\nEnter education title: ")
  major = auth.logged_in_user['major']
  university = auth.logged_in_user['university']
  about = input("\nTell your friends about yourself: ")
  experience = input("\nWhat experience do you have?: ")
  education = input("\nEnter Education:")
  
  return profileModel.profile(user, title, major, university, about, experience, education)