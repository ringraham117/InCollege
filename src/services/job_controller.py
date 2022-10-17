import json

import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.constants.success_messages as successMessage


def clear_jobs_list():

    # Stores a reference to the jobs dictionary
    database = get_database_object()
    
    # Sets the jobs list to be an empty list
    database["jobs"] = []
    
    # Updates the jobs database 
    update_database_object(database)

def is_database_limit_reached():
    database = get_database_object()
    return len(database["jobs"]) >= 5


def get_database_object():
    database_file = open('databases/job_post.json')
    file_data = database_file.read()
    return json.loads(file_data)


def update_database_object(updated_database):
    database_file = open('databases/job_post.json', 'w')
    json.dump(updated_database, database_file, indent=2)


def add_job(job):
    if (is_database_limit_reached()):
        notificationHandler.display_notification(
            errorMessages.JOB_DATABASE_LIMIT_MESSAGE)
        return

    database = get_database_object()
    database["jobs"].append(job.__dict__)
    update_database_object(database)
    notificationHandler.display_notification(
        successMessage.SUCCESSFUL_JOB_POSTING)
