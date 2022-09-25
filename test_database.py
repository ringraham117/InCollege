import database as db

def test_user_exists():
    
    user = "sjfdjsdflkl"
    passwd = "ksjdbghkbhbbfk"
    assert db.user_exists_in_db(user, passwd) == False

def test_add_user():
    first_name = "Steve"
    last_name = "Jobs"
    username = "thisisausername"
    password = "thisisapassword"

    db.clear_db()
    assert db.user_exists_in_db(username, password) == False
    
    db.add_user_to_db(first_name, last_name, username, password)
    assert db.user_exists_in_db(username, password) == True

def test_can_add_more_users():
    db.clear_db()
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
