import database as db
import json
import pytest

def test_user_exists():
    
    user = "sjfdjsdflkl"
    passwd = "ksjdbghkbhbbfk"
    assert db.user_exists_in_db(user, passwd) == False

def test_add_user():
    username = "thisisausername"
    password = "thisisapassword"
    assert db.user_exists_in_db(username, password) == False
    db.add_user_to_db(username, password)
    assert db.user_exists_in_db(username, password) == True


def test_can_add_more_users():

    # Clears the database
    database = {"users_list": []}

    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent=2)

    assert len(database["users_list"]) == 0
    assert db.can_add_more_users() == True

    # Adds 5 users to the database
    db.add_user_to_db("user1", "password")
    db.add_user_to_db("user2", "password")
    db.add_user_to_db("user3", "password")
    db.add_user_to_db("user4", "password")
    db.add_user_to_db("user5", "password")

    assert db.can_add_more_users() == False
