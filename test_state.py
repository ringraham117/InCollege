import database as db
import json
import state
import pytest


def test_incorrect_login(capsys, monkeypatch):
  database = {"users_list": []}
  
  with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent=2)

  db.add_user_to_db("user5", "Password1!")

  # This sends the inputs in the order that you specify
  # Make a list of values to simulate writing to the terminal 
  # Purposely fail the login and then login successfully to end the login loop.
  inputs = iter(["wrong", "passwrong", "user5", "Password1!", "1", "1"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))
  
  # Call the function to simulate logging in
  state.goto_logging_in_state()

  # Read what was printed to the terminal
  stdout, stderr = capsys.readouterr()

  # Assert statement
  # I think you need to remove the spaces from the beginning of each line. 
  assert stdout == '''
Login:
Incorrect username/password, please try again.

Login:

You have successfully logged in.

What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill

Under Construction.
'''

@pytest.mark.parametrize(
    ('user', 'passw'),
    (('user1', 'password'), ('user2', 'password')),
)
def test_logging_in(capsys, monkeypatch, user, passw):

    # Empties the database
    # Defines an empty dictionary with the correct format
    database = {"users_list": []}

    # Writes the empty dictionary to the JSON file
    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent=2)

    db.add_user_to_db(user,passw)
  
    # Values simulate writing to the terminal
    inputs = iter([user, passw, "3", "1"])
    
    # Simulates entering the "inputs" into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Call the function to simulate logging in
    state.goto_logging_in_state()
    
    # Reads what was printed to the terminal
    stdout, stderr = capsys.readouterr()
    
    assert stdout == '''
Login:

You have successfully logged in.

What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill

What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Under construction.
'''

@pytest.mark.parametrize(('user_selection'), ((1), (2), (3)))
def test_logged_in(capsys, monkeypatch, user_selection):
  monkeypatch.setattr('builtins.input', lambda _: user_selection)
  state.goto_logged_in_state()
  
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
'''

@pytest.mark.parametrize(('user_selection'), ((1), (2), (3), (4), (5)))
def test_learn_skill(capsys, monkeypatch, user_selection):
    monkeypatch.setattr('builtins.input', lambda _: user_selection)
    state.goto_learn_a_skill_state()
    
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen
'''


# What do you want to do?
# 1. Search for an internship/job
# 2. Find someone you know
# 3. Learn a new skill

def test_create_account(capsys, monkeypatch):

    # Defines an empty dictionary with the correct format
    database = {"users_list": []}

    # Writes the empty dictionary to the JSON file
    with open("users.json", "w") as myFile:
        json.dump(database, myFile, indent=2)
  
    inputs = iter(["user5", "Password1!", "1", "user5", "Password1!", "3", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    state.goto_create_new_account_state()
    
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Create a new user:
Account successfully created.

InCollege
---------
1. Login
2. Sign up

Login:

You have successfully logged in.

What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill

What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Under construction.
'''

  