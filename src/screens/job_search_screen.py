import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.job_controller as jobController

import src.models.job_model as jobModel

screen_options = ["Post a Job"]


def screen():
  screen_display = "Job Search & Internship"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  elif user_selection in screen_options:
    if user_selection == "Post a Job":
      job = get_user_job_data()
      jobController.add_job(job)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
  screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens



def get_user_job_data():
  user = auth.logged_in_user['username']
  title = input("\nEnter job title: ")
  description = input("Enter job description: ")
  employer = input("Enter employer: ")
  location = input("Enter location: ")
  salary = input("Enter salary: ")
  return jobModel.Job(user, title, description, employer, location, salary)
