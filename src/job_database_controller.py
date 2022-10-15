import json
import src.models.job_model as job_model

def add_job_to_db(user, title, description, employer, location, salary):
  
  new_job = job_model.Job(user, title, description, employer, location, salary)
  database = get_database()
  database["jobs_list"].append(new_job.__dict__)

  # Updates the JSON file
  with open("databases/jobs.json", "w") as myFile:
      json.dump(database, myFile, indent=2)

def can_add_more_jobs():
  return True

def clear_jobs_list():
    empty_jobs_list = {"jobs_list": []}

    # Opens the JSON file in write mode
    with open("databases/jobs.json", 'w') as data_file:
        json.dump(empty_jobs_list, data_file, indent=2)

def get_database():
  with open("databases/jobs.json") as data_file:
      database = json.load(data_file)
      return database

def get_jobs_dictionary():
  with open("databases/jobs.json") as data_file:
        dictionary = json.load(data_file)
        return dictionary

def get_jobs_list():
    with open("databases/jobs.json") as data_file:
        database = json.load(data_file)
        return database["jobs_list"]


def job_exists_in_db(title, description, employer, location, salary):
    for job in get_jobs_list():
      if job["title"] == title \
      and job["description"] == description \
      and job["employer"] == employer \
      and job["location"] == location \
      and job["salary"] == salary:

        return True

    return False