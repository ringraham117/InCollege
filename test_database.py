import src.job_database_controller as job_db
import src.user_database_controller as user_db
import src.models.job_model as job_model
import src.pages.job_post_page as job_post_page

def test_user_exists():
    
    user = "sjfdjsdflkl"
    passwd = "ksjdbghkbhbbfk"
    assert user_db.user_exists_in_db(user, passwd) == False

def test_add_user():
    first_name = "Steve"
    last_name = "Jobs"
    username = "thisisausername"
    password = "thisisapassword"

    user_db.clear_users_list()
    assert user_db.user_exists_in_db(username, password) == False
    
    user_db.add_user_to_db(first_name, last_name, username, password)
    assert user_db.user_exists_in_db(username, password) == True


def test_can_add_more_users():
    user_db.clear_users_list()
    users_list = user_db.get_users_list()
  
    assert len(users_list) == 0
    assert user_db.can_add_more_users() == True

    # Adds 5 users to the database
    user_db.add_user_to_db("firstName", "lastName", "user1", "password")
    user_db.add_user_to_db("firstName", "lastName", "user2", "password")
    user_db.add_user_to_db("firstName", "lastName", "user3", "password")
    user_db.add_user_to_db("firstName", "lastName", "user4", "password")
    user_db.add_user_to_db("firstName", "lastName", "user5", "password")

    assert user_db.can_add_more_users() == False

def test_job_exists_in_db():
    job_db.clear_jobs_list()
    assert job_db.job_exists_in_db("SWE", "Write code", "Startup576", "Silicon Valley", "Enough") == False

    new_job = job_model.Job("cool_user", "SWE", "Write code", "Startup576", "Silicon Valley", "Enough")
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)

    assert job_db.job_exists_in_db("SWE", "Write code", "Startup576", "Silicon Valley", "Enough") == True

def test_job_storage_limit():
    job_db.clear_jobs_list()
    jobs_dictionary = job_db.get_jobs_dictionary()
    assert job_post_page.is_database_limit_reached(jobs_dictionary) == False

    # Adds 5 jobs to the database
    new_job = job_model.Job("cool_user", "SWE", "Write code", "Startup576", "Silicon Valley", "Lots!")
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)
    
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)
    job_post_page.store_job_database(job_db.get_jobs_dictionary(), new_job)

    # Update the jobs dictionary
    jobs_dictionary = job_db.get_jobs_dictionary()   
  
    assert job_post_page.is_database_limit_reached(jobs_dictionary) == True

# Epic #3 Test
def test_guest_controls_storage():
    user_db.clear_users_list()
    user_db.add_user_to_db("Eric", "Forman", "Eric", "password")
    
    users_list = user_db.get_users_list()
    test_user = users_list[0]
    
    assert test_user["sms"] == True 
    assert test_user["email"] == True
    assert test_user["targeted_ads"] == True

# Epic #3 Test
def test_default_language_setting():
    user_db.clear_users_list()
    user_db.add_user_to_db("Harry", "Potter", "Wizard", "password")

    users_list = user_db.get_users_list()
    test_user = users_list[0]

    assert test_user["language"] == "English"