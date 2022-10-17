import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

screen_options = [
  screenNames.SIGNUP_SCREEN, screenNames.ABOUT_SCREEN, screenNames.BLOG_SCREEN,
  screenNames.CAREERS_SCREEN, screenNames.DEVELOPERS_SCREEN,
  screenNames.HELP_CENTER_SCREEN, screenNames.PRESS_SCREEN
]


def screen():
  screen_display = "Welcome to general screen!"
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
