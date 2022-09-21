import json
import state
import src.models.job_model as job_model
import src.pages.job_search_page as job_search_page


def display_job_post_page():
    job_database = open_database_file()

    if is_database_limit_reached(job_database):
        print("\nUnable to add more jobs, database limit exceeded")
    else:
        created_job = get_job_data_from_user()
        store_job_database(job_database, created_job)
        print("Job Posted Successfully!\n")

    job_search_page.display_job_search_page()


def get_job_data_from_user():
    user = state.loggedInUser
    title = input("\nEnter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")
    return job_model.JobPostDescription(user, title, description, employer,
                                        location, salary)


def store_job_database(job_database, created_job):
    job_database["jobs"].append(created_job.__dict__)
    with open("databases/job_posting.json", "w") as myFile:
        json.dump(job_database, myFile, indent=2)


def is_database_limit_reached(job_database):
    return len(job_database["jobs"]) > 5


def open_database_file():
    with open("databases/job_posting.json") as data_file:
        job_data = json.load(data_file)
    return job_data
