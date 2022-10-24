import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.models.user_model as userModel
import src.authentication.auth as auth
import src.shared.password_validator as passwordValidator
import src.constants.success_messages as successMessage
import src.services.user_controller as userController
import src.services.unique_id_controller as uniqueIdController
import src.shared.format_input_first_upper as formatToFirstUpper

import src.models.job_model as jobModel


def screen():
  screen_display = ""
  screen_options = get_screen_options()

  if auth.logged_in_user == None:
    screen_display = "Welcome to signup screen, select from the options below!"
  else:
    screen_display = "You are already signed in!"

  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


# def handle_signup():
#     if (screen_exists(user_selection)):
#         navigate_user(user_selection)
#     elif user_selection == "Sign Up":
#         handle_signup()
#     else:
#         notificationHandler.display_notification(
#             errorMessages.INVALID_SELECTION_MESSAGE)
#         screen()


def handle_signup():
  user = get_user_signup_data()
  if passwordValidator.is_password_valid(user.password):
    userController.add_user(user)
  else:
    notificationHandler.display_notification(
      errorMessages.WEAK_PASSWORD_MESSAGE)

  screen()


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  elif user_selection == "Sign Up":
    handle_signup()
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def get_user_signup_data():
  unique_id = uniqueIdController.generate_unique_id()
  username = input("Username: ")
  password = input("Password: ")
  first_name = input("First Name: ")
  last_name = input("Last Name: ")
  university = input("University: ")
  major = input("Major: ")

  major = formatToFirstUpper.format_input_first_upper(major)
  university = formatToFirstUpper.format_input_first_upper(university)

  return userModel.User(unique_id=unique_id,
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        university=university,
                        major=major)


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens


def get_screen_options():
  screen_options = []
  if auth.logged_in_user == None:
    screen_options.append("Sign Up")
  return screen_options
