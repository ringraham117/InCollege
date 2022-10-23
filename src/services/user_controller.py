import json

import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.authentication.auth as auth
import src.shared.object_to_dict_converter as objectToDictConverter


def clear_users_list():
    database = {"users": []}

    # Opens the JSON file in write mode
    with open("databases/user_credentials.json", 'w') as data_file:
        json.dump(database, data_file, indent=2)


def is_database_limit_reached():
    database = get_database_object()
    return len(database["users"]) >= 10


def get_database_object():
    database_file = open('databases/user_credentials.json')
    file_data = database_file.read()
    return json.loads(file_data)


def update_database_object(updated_database):
    database_file = open('databases/user_credentials.json', 'w')
    json.dump(updated_database, database_file, indent=2)


def add_user(user):

    if (is_database_limit_reached()):
        notificationHandler.display_notification(
            errorMessages.USER_DATABASE_LIMIT_MESSAGE)
        return

    database = get_database_object()
    user_dict = objectToDictConverter.job_to_dict(user)
    database["users"].append(user_dict)
    update_database_object(database)


def get_user_by_id(user_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            return database_user
    return None


def get_user_by_username(username):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["username"] == username:
            return database_user
    return None


def get_users_by_first_name(first_name):
    users = []
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["profile"]["first_name"] == first_name:
            users.append(database_user)
    return users


def get_users_by_last_name(last_name):
    users = []
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["profile"]["last_name"] == last_name:
            users.append(database_user)
    return users


def get_users_by_university(university):
    users = []
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["profile"]["university"] == university:
            users.append(database_user)
    return users


def get_users_by_major(major):
    users = []
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["profile"]["major"] == major:
            users.append(database_user)
    return users


def send_friend_request(username):
    sender_id = auth.logged_in_user["user_id"]
    receiver = get_user_by_username(username)
    if receiver is None:
        notificationHandler.display_notification(
            errorMessages.USER_NOT_FOUND_MESSAGE)
        return
    else:
        if (sender_id == receiver["user_id"]):
            notificationHandler.display_notification(
                "Why are you trying to add yourself as a friend?")
            return
        receiver_id = receiver["user_id"]
        database = get_database_object()
        for database_user in database["users"]:
            if database_user["user_id"] == receiver_id:
                if sender_id in database_user["friend_requests"]:
                    notificationHandler.display_notification(
                        "Friend request already sent!")
                elif sender_id in database_user["friends"]:
                    notificationHandler.display_notification(
                        "You are already friends with this user!")
                else:
                    database_user["friend_requests"].append(sender_id)
                    notificationHandler.display_notification(
                        "Friend request successfully sent!")
                    update_database_object(database)


def get_user_friend_requests(user_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            return database_user['friend_requests']
    return None


def get_user_friends(user_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            return database_user['friends']
    return None


def is_valid_job_id(user_id, job_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            for job in database_user["profile"]['experience']:
                if job["job_id"] == job_id:
                    return True
    return False


def get_user_experience(user_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            return database_user['profile']["experience"]
    return None


def add_user_to_friends(user_id, request_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            database_user["friends"].append(request_id)
    update_database_object(database)


def delete_user_friend(user_id, friend_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            database_user["friends"].remove(friend_id)
    update_database_object(database)


def delete_user_friend_request(user_id, request_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            database_user["friend_requests"].remove(request_id)
    update_database_object(database)


def set_user_language(user_id, language):
    user = get_user_by_id(user_id)
    if user is None:
        notificationHandler.display_notification(
            errorMessages.INVALID_USER_ID_MESSAGE)
        return
    else:
        user["language"] = language
        database = get_database_object()
        for database_user in database["users"]:
            if database_user["user_id"] == user_id:
                database_user["language"] = language
        update_database_object(database)


def set_user_sms(user_id, sms):
    database = get_database_object()
    for user in database["users"]:
        if user["user_id"] == user_id:
            user['settings']["sms_notifications"] = sms
    update_database_object(database)


def set_user_email(user_id, email):
    database = get_database_object()
    for user in database["users"]:
        if user["user_id"] == user_id:
            user['settings']["email_notifications"] = email
    update_database_object(database)


def set_user_ads(user_id, ads):
    database = get_database_object()
    for user in database["users"]:
        if user["user_id"] == user_id:
            user['settings']["ad_notifications"] = ads
    update_database_object(database)


def get_user_by_first_last_name(first_name, last_name):
    database = get_database_object()
    for user in database["users"]:
        if user['profile']["first_name"] == first_name and user['profile']["last_name"] == last_name:
            return user
    return None


def set_user_title(username, title):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:
            user['profile']["title"] = title
    update_database_object(database)


def set_user_about(username, about):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            user['profile']["about"] = about
    update_database_object(database)


def set_user_experience(username, experience):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            for exp in experience:
                user['profile']["experience"].append(exp.__dict__)
    update_database_object(database)


def set_user_education(username, education):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            for school in education:
                user['profile']["education"].append(school.__dict__)

    update_database_object(database)


def set_active_profile(username, active_profile):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            user["active_profile"] = active_profile
    update_database_object(database)


def set_user_major(username, major):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            user['profile']["major"] = major
    update_database_object(database)


def set_past_job_title(username, job_index, title):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["job_title"] = title

    update_database_object(database)


def set_past_job_employer(username, job_index, employer):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["job_employer"] = employer

    update_database_object(database)


def set_past_job_start_date(username, job_index, start_date):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["start_date"] = start_date

    update_database_object(database)


def set_past_job_end_date(username, job_index, end_date):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["end_date"] = end_date

    update_database_object(database)


def set_past_job_location(username, job_index, location):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["location"] = location

    update_database_object(database)


def set_past_job_description(username, job_index, description):
    database = get_database_object()

    for user in database["users"]:
        if user["username"] == username:

            user_past_job_list = user["experience"]
            selected_job = user_past_job_list[job_index]
            selected_job["description"] = description

    update_database_object(database)


def set_user_university(username, university):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            user["university"] = university
    update_database_object(database)


def update_user_experience(username, job_id, updated_exp):
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            for exp in user['profile']["experience"]:
                if exp["job_id"] == job_id:
                    exp["title"] = updated_exp.title
                    exp["employer"] = updated_exp.employer
                    exp["start_date"] = updated_exp.start_date
                    exp["end_date"] = updated_exp.end_date
                    exp["location"] = updated_exp.location
                    exp["description"] = updated_exp.description
    update_database_object(database)


def is_valid_edu_id(user_id, edu_id):
    database = get_database_object()
    for database_user in database["users"]:
        if database_user["user_id"] == user_id:
            for job in database_user["profile"]['education']:
                if job["edu_id"] == edu_id:
                    return True
    return False


def update_user_education(username, edu_id, updated_edu):
    print(updated_edu.__dict__)
    database = get_database_object()
    for user in database["users"]:
        if user["username"] == username:
            for edu in user['profile']["education"]:
                if edu["edu_id"] == edu_id:
                    edu["school"] = updated_edu.school
                    edu["degree"] = updated_edu.degree
                    edu['years'] = updated_edu.years
    update_database_object(database)


def add_job_to_user(user_id, job_id):
    database = get_database_object()
    for user in database["users"]:
        if user["user_id"] == user_id:
            user["jobPosts"].append(job_id)
    update_database_object(database)
