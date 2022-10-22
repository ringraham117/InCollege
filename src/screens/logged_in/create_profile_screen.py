import src.authentication.auth as auth
import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.shared.format_input_first_upper as formatToFirstUpper


def screen():
  screen_options = []

  screen_display = "Create/View Your Profile"
  user = auth.logged_in_user

  # In which case is "create profile" not in the screen options?
  if "Create Profile" not in screen_options:
    if user['has_profile'] == False:
      screen_options.append("Create User Profile")
    else:
      screen_display = "This is the profile of " + user[
        'first_name'] + " " + user['last_name'] + "!\n" + get_profile_display(
          user['title'], user['university'], user['major'],
          user['about'], user['school'], user['degree'], user['years'])
      for option in get_edit_profile_options():
        screen_options.append(option)

  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  username = auth.logged_in_user['username']

  if (screen_exists(user_selection)):
    navigate_user(user_selection)

  elif user_selection == "Create User Profile":
    title, about, experience, school, degree, years = get_user_profile_data()
    set_user_profile_data(username, title, about, experience, school, degree,
                          years, True)

  elif user_selection == "Edit Title":
    title = input("\nEnter title: ")
    userController.set_user_title(username, title)

  elif user_selection == "Edit Major":
    major = input("\nEdit Major: ")
    major = formatToFirstUpper.format_input_first_upper(major)
    userController.set_user_major(username, major)

  elif user_selection == "Edit About":
    about = input("\nEdit About: ")
    userController.set_user_about(username, about)

  elif user_selection == "Edit Experience":

    # Go to to the "edit experience" screen
    navigate_user(screenNames.EDIT_EXPERIENCE_SCREEN)

  elif user_selection == "Edit Education":
    navigate_user(screenNames.EDIT_EDUCATION_SCREEN)

    print("\nEdit Education: ")
    school = input("\n\t\tEnter school: ")
    degree = input("\n\t\tEnter degree: ")
    years = input("\n\t\tEnter years: ")
    userController.set_user_education(username, school, degree, years)

  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)

  # What does this function do?
  auth.update_logged_in_user()
  screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens


def get_user_education():
  print("\nEnter your education")
  school = input("\n\t\tEnter school: ")
  degree = input("\n\t\tEnter degree: ")
  years = input("\n\t\tEnter years: ")

  return school, degree, years


def get_user_profile_data():
  title = input("\nEnter title: ")
  about = input("\nEnter About: ")
  experience = "TESTING"
  #experience = input("\nEnter experience: ")
  #education = input("\nEnter education:")
  print("\nEnter your education")
  school = input("\n\t\tEnter school: ")
  degree = input("\n\t\tEnter degree: ")
  years = input("\n\t\tEnter years: ")

  return title, about, experience, school, degree, years


def set_user_profile_data(username, title, about, experience, school, degree,
                          years, has_profile):
  userController.set_user_title(username, title)
  userController.set_user_about(username, about)
  #userController.set_user_experience(username, experience)
  userController.set_user_education(username, school, degree, years)
  userController.set_has_profile(username, has_profile)


def get_profile_display(title, university, major, about, school,
                        degree, years):
  return "\nTitle: " + title + "\nUniversity: " + university + "\nMajor: " + major + "\nAbout: " + about + "\nExperience: " + "TESTING" + "\nEducation: " + school + ", " + degree + ", " + years


def get_edit_profile_options():
  return [
    "Edit Title", "Edit Major", "Edit About", "Edit Experience",
    "Edit Education"
  ]
