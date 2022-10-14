import json
import src.models.job_model as job_model

def add_job_to_db(user, title, description, employer, location, salary):
  
  new_job = job_model.Job(user, title, description, employer, location, salary)
  database = get_database()
  database["jobs_list"].append(new_job.__dict__)

  # Updates the JSON file
  with open("databases/jobs.json", "w") as myFile:
      json.dump(database, myFile, indent=2)

def get_database():
  with open("databases/jobs.json") as data_file:
      database = json.load(data_file)
      return database

def can_add_more_jobs():
  return True