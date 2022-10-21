import src.authentication.auth as auth
import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.models.user_model as userModel
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
          user['title'], user['university'], user['major'], user['experience'],
          user['about'], user['education'])
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
    title, about, experience, education = get_user_profile_data()
    set_user_profile_data(username, title, about, experience, education, True)

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

    # Experience section (Each job needs a unique ID) (Could be as simple as 1, 2, 3)

    # Provide the user with a list of jobs to edit (Include the title of the job instead of just "Job 1")
    # Issue: This menu is not cleared before showing the next screen
    # Potential solution: Transform the menu into its own screen so that it works more smoothly with the display handler (User input would be read in on the new screen)
    # Alternative solution: Define the menu here and just call the "clear screen" function here (Downside: There would not be a built-in "previous screen" option)

    # Goal: Include a message at the top of the screen to indicate which job is being edited
      # Potential solution: Include one screen for choosing a job and then another screen for editing job details

    print("0. Job 1")
    print("1. Job 2")
    print("2. Job 3")

    # Allow the user to select a job
    job_selection = input("Select a job: ")

    # Converts from string to int
    job_index = int(job_selection)

    # Get a reference to the selected job from the database
    # Assume "experience" is a list a jobs (indexed starting from 0)
    selected_job = auth.logged_in_user["profile"]["experience"][job_index]

    # Allow the user edit attributes of that job (could be a new screen)
    # Go to a new screen to edit the job (Upside: Automatically clears the screen and has built-in "previous option") (Downside: You'd have to pass the selected job to the new screen)
    # Alternative: Print menus here and then handle user input in a different function
    navigate_user(screenNames.EDIT_JOB_SCREEN)

    experience = input("\nEdit Experience: ")
    userController.set_user_experience(username, experience)

  elif user_selection == "Edit Education":
    navigate_user(screenNames.EDIT_EDUCATION_SCREEN)

    education = input("\nEnter Education: ")
    userController.set_user_education(username, education)

  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)

  auth.update_logged_in_user()
  screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens


def get_user_profile_data():
  title = input("\nEnter title: ")
  about = input("\nEnter About: ")
  experience = input("\nEnter experience: ")
  education = input("\nEnter education:")

  return title, about, experience, education


def set_user_profile_data(username, title, about, experience, education,
                          has_profile):
  userController.set_user_title(username, title)
  userController.set_user_about(username, about)
  userController.set_user_experience(username, experience)
  userController.set_user_education(username, education)
  userController.set_has_profile(username, has_profile)


def get_profile_display(title, university, major, about, experience,
                        education):
  return "\nTitle: " + title + "\nUniversity: " + university + "\nMajor: " + major + "\nAbout: " + about + "\nExperience: " + experience + "\nEducation: " + education


def get_edit_profile_options():
  return [
    "Edit Title", "Edit Major", "Edit About", "Edit Experience",
    "Edit Education"
  ]


# user1.profile.title = "abc"
# user1["profile"]["title"] = "abc"
# user1: {
#   profile: {
#    title: "abc"
#  }
# }
