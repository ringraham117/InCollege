import database as db
import src.models.job_model as job_model
import src.pages.job_post_page as job_post_page

def test_user_exists():
    
    user = "sjfdjsdflkl"
    passwd = "ksjdbghkbhbbfk"
    assert db.user_exists_in_db(user, passwd) == False

def test_add_user():
    first_name = "Steve"
    last_name = "Jobs"
    username = "thisisausername"
    password = "thisisapassword"

    db.clear_users_list()
    assert db.user_exists_in_db(username, password) == False
    
    db.add_user_to_db(first_name, last_name, username, password)
    assert db.user_exists_in_db(username, password) == True


def test_can_add_more_users():
    db.clear_users_list()
    users_list = db.get_users_list()
  
    assert len(users_list) == 0
    assert db.can_add_more_users() == True

    # Adds 5 users to the database
    db.add_user_to_db("firstName", "lastName", "user1", "password")
    db.add_user_to_db("firstName", "lastName", "user2", "password")
    db.add_user_to_db("firstName", "lastName", "user3", "password")
    db.add_user_to_db("firstName", "lastName", "user4", "password")
    db.add_user_to_db("firstName", "lastName", "user5", "password")

    assert db.can_add_more_users() == False

def test_job_exists_in_db():
    db.clear_jobs_list()
    assert db.job_exists_in_db("SWE", "Write code", "Startup576", "Silicon Valley", "Enough") == False

    new_job = job_model.JobPostDescription("cool_user", "SWE", "Write code", "Startup576", "Silicon Valley", "Enough")
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)

    assert db.job_exists_in_db("SWE", "Write code", "Startup576", "Silicon Valley", "Enough") == True

def test_job_storage_limit():
    db.clear_jobs_list()
    jobs_dictionary = db.get_jobs_dictionary()
    assert job_post_page.is_database_limit_reached(jobs_dictionary) == False

    # Adds 5 jobs to the database
    new_job = job_model.JobPostDescription("cool_user", "SWE", "Write code", "Startup576", "Silicon Valley", "Lots!")
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)
    
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(db.get_jobs_dictionary(), new_job)

    # Update the jobs dictionary
    jobs_dictionary = db.get_jobs_dictionary()   
  
    assert job_post_page.is_database_limit_reached(jobs_dictionary) == True
