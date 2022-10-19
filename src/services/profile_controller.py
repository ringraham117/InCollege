import json

import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.authentication.auth as auth


def clear_profile_list():
  database = {"profiles": []}

  # Opens the JSON file in write mode
  with open("databases/user_profiles.json", 'w') as data_file:
    json.dump(database, data_file, indent=2)

def get_database_object():
  database_file = open('databases/user_profiles.json')
  file_data = database_file.read()
  return json.loads(file_data)


def update_database_object(updated_database):
  database_file = open('databases/user_profiles.json', 'w')
  json.dump(updated_database, database_file, indent=2)


def add_profile(profile):
  database = get_database_object()
  database["profiles"].append(profile.__dict__)
  update_database_object(database)

