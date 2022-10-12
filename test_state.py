import database as db
import json
import state
import pytest

## ALL TEST CASES in this file pass EPIC 3 - test_state.py
# Note: Use "Ctrl + /" to comment or uncomment multiple lines at one time.
# -----------------------------------------------------------------------

# pytest -vv test_state.py::test_create_account
#so just use a :: to specify the particular test case you want to test
#-----------------------------------------------------------------------


# Epic #2 Test
# Tester: Ryan - Epic 3 - Done
def test_success_story(capsys, monkeypatch):

    inputs = iter(["7"])

    # Simulate entering those values into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    #call the function
    state.goto_start_menu_state()

    #Read what was printed to the terminal
    stdout, stderr = capsys.readouterr()

    #assert output
    assert stdout == '''

I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #1 Test
# Tester: Ryan - Epic 3 - Done
def test_incorrect_login(capsys, monkeypatch):

    # Clear the database to start from a controlled state
    db.clear_users_list()
    
    # Adds a user to the system
    db.add_user_to_db("Tom", "Cruise", "maverick", "topGun22!")

    # This sends the inputs in the order that you specify
    # Make a list of values to simulate writing to the terminal
    # Bad login --> Good login --> Logout --> Exit
    inputs = iter(["wrong", "passwrong", "maverick", "topGun22!", "6", "7"])

    # Simulate entering those values into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to simulate logging in
    state.goto_logging_in_state()

    # Read what was printed to the terminal
    stdout, stderr = capsys.readouterr()

    # Assert statement    
    assert stdout == '''
Login:
Incorrect username/password, please try again.

Login:

You have successfully logged in.

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #1 Test
# Tester: Ryan - Epic 3 - Done
def test_logging_in(capsys, monkeypatch):

    # Empties the database
    # Defines an empty dictionary with the correct format
    database = {"users_list": []}

    # Writes the empty dictionary to the JSON file
    with open("databases/user_credentials.json", "w") as myFile:
        json.dump(database, myFile, indent=2)

    # db.add_user_to_db(user, passw)
    db.add_user_to_db("Brad", "Pitt", "BPitt", "movieStar1!")

    # Values simulate writing to the terminal
    inputs = iter(["BPitt", "movieStar1!", "6", "7"])

    # Simulates entering the "inputs" into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to simulate logging in
    state.goto_logging_in_state()

    # Reads what was printed to the terminal
    stdout, stderr = capsys.readouterr()

    assert stdout == '''
Login:

You have successfully logged in.

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''



# Epic #1 Test
# Tester: Ryan - Epic 3 - Done
def test_logged_in(capsys, monkeypatch):

    inputs = iter(["6", "7"])
  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_logged_in_state()

    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''



# Epic #1 Test
# Tester: Ryan - Epic 3 - Done
@pytest.mark.parametrize(('user_selection'), ((1), (2), (3), (4), (5)))
def test_learn_skill(capsys, monkeypatch, user_selection):
    monkeypatch.setattr('builtins.input', lambda _: user_selection)
    state.goto_learn_a_skill_state()

    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen
'''


# Epic #1 Test
# Tester: Ryan - Epic 3 - Done
def test_create_account(capsys, monkeypatch):

    # Defines an empty dictionary with the correct format
    database = {"users_list": []}

    # Writes the empty dictionary to the JSON file
    with open("databases/user_credentials.json", "w") as myFile:
        json.dump(database, myFile, indent=2)


    inputs = iter(
        ["Kim", "Kardashian", "kimK", "fakeBody1!", "1", "kimK", "fakeBody1!", "6", "7"])
  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_create_new_account_state()

    stdout, stderr = capsys.readouterr()
  
    assert stdout == '''
Create a new user:
Account successfully created.


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Login:

You have successfully logged in.

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''

# Epic #2 Test
# test back option for web development -skill 1
def test_goto_learn_web_dev_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "6", "7"])
  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    state.goto_learn_web_dev_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn Web Development
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu

Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''  


### Tester:Namira - PASSED EPIC 3 TEST
# Epic #2 Test
#test for learn coding back option - skill 2
def test_goto_learn_coding_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_learn_coding_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn Coding
------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu

Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #2 Test
#tests back option for commmunication skill - skill 3
def test_goto_learn_communication_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_learn_communication_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn Communication
-------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu

Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''    



# Epic #2 Test
#tests back option for resume critique - skill 4
## Tester : Namira - Epic 3 - PASSED
def test_goto_learn_resume_critique_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_learn_resume_critique_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn Resume Critique
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu

Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''



# Epic #2 Test
# tests back option for learn microsoft excel - skill 5
def test_goto_learn_excel_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    state.goto_learn_excel_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn Microsoft Excel
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu

Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''



# Epic #2 Test
#tests display of inCollege video
#tests back option in watch video state
## Tester: Namira - passed epic 3
def test_goto_watch_video_state(capsys, monkeypatch):

    # This sends the inputs in the order that you specify
    # Make a list of values to simulate writing to the terminal
    inputs = iter(["3", "1", "2", "7"])

    # Simulate entering those values into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to simulate logging in
    state.goto_start_menu_state()

    stdout, stderr = capsys.readouterr()
    assert stdout == '''

I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Play the "Why Join InCollege?" video
----------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu
Video is now playing.

Play the "Why Join InCollege?" video
----------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #2 Test
#tests back option for find people you may know
def test_goto_find_someone_you_know_state(capsys, monkeypatch):
    inputs = iter(["2", "6", "7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    state.goto_find_someone_you_know_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Find someone you know
-----------------------
What do you want to do?
1. Continue
2. Return to Top-level Menu

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''

# Epic #2 Test
## Tester: Namira - PASSED EPIC 3 TEST
#tests back option for search menu
def test_goto_search_for_user_state(capsys, monkeypatch):
    inputs = iter(["2", "7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    state.goto_search_for_user_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Search for an active InCollege user
-------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''

# Epic #2 Test
#tests back option for learn a new skill
## Tester: Namira - PASSED EPIC 3 TEST
def test_goto_learn_a_skill_state(capsys, monkeypatch):
    inputs = iter(["6", "6", "7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    state.goto_learn_a_skill_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Learn a Skill Menu
------------------
What skill do you want to learn?
1. Web Development
2. Coding
3. Communication
4. Resume Critique
5. Microsoft Excel
6. Return to Previous Screen

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #2 Test
#tests back option in top-level menu
## Tester: Namira - PASSED EPIC 3 TEST
def test_top_level_back(capsys, monkeypatch):
    inputs = iter(["6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    #   menu.print_top_level_menu()
    state.goto_logged_in_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


## Tester: Namira - PASSED EPIC 3 TEST
# Epic #2 Test
#tests back option in find a job
def test_findJob_back(capsys, monkeypatch):
    inputs = iter(["1", "2", "6", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_logged_in_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out

What do you want to do?

1. Post a job
2. Return to previous page


Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #2 Test
## Tester: Namira - PASSED EPIC 3 TEST
#tests the search option of the start menu
#tests the back option of the search
#if user is found, prompt user to login/signup
def test_search(capsys, monkeypatch):
    # Empties the database
    # Defines an empty dictionary with the correct format
    database = {"users_list": []}

    # Writes the empty dictionary to the JSON file
    with open("databases/user_credentials.json", "w") as myFile:
        json.dump(database, myFile, indent=2)

    db.add_user_to_db("Elon", "Musk", "tesla", "toTheMoon1!")

    inputs = iter(
        ["4", "1", "Elon", "Musk", "3", "4", "1", "not", "insystem", "2", "7"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    state.goto_start_menu_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''

I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Search for an active InCollege user
-------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu

They are a part of the InCollege system.

Join your friends on the InCollege system!
------------------------------------------
1. Login
2. Sign up
3. Return to Start Menu


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Search for an active InCollege user
-------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu

They are not yet a part of the InCollege system.

Search for an active InCollege user
-------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''


# Epic #2 Test
## Tester: Namira - passed EPIC 3 TEST
def test_post_a_job(capsys, monkeypatch):

    db.clear_jobs_list()

    # Login --> Search for job --> Post a job --> *Enter job details* --> Return to top-level menu --> Logout --> Exit
    inputs = iter([
        "tesla", "toTheMoon1!", "1", "1", "Data Analyst",
        "SQL, programming required", "Tesla", "LA", "70000", "2", "6", "7"
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Goes to the logging in state
    state.goto_logging_in_state()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Login:

You have successfully logged in.

Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out

What do you want to do?

1. Post a job
2. Return to previous page

Job Posted Successfully!


What do you want to do?

1. Post a job
2. Return to previous page


Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Useful Links
5. InCollege Important Links
6. Log out


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Useful Links
6. InCollege Important Links
7. Exit

Program is exiting!
'''