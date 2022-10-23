import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.id_controller as idController
import src.models.job_model as jobModel
import src.services.user_controller as userController
import src.services.job_controller as jobController

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
            user_id = auth.logged_in_user['user_id']
            job = get_user_job_data()
            jobController.post_job(job)
            userController.add_job_to_user(user_id, job.job_id)
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
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")
    job_id = idController.generate_job_id()
    return jobModel.Job(job_id=job_id, user=user, title=title, description=description, employer=employer, location=location, salary=salary)
