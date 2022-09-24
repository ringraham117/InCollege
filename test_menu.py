import menu


def test_start_menu(capsys):
    menu.print_start_menu()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
Welcome to InCollege
--------------------
1. Login
2. Sign up
3. Play video ("Why Join InCollege?")
4. Search for InCollege users
5. Exit
'''

  
def test_print_top_level_menu(capsys):
  menu.print_top_level_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Top-level Menu
--------------
What do you want to do?
1. Search for an internship/job
2. Find someone you know
3. Learn a new skill
4. Log out
'''

def test_print_skills_menu(capsys):
  menu.print_skills_menu()
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
def test_print_video_menu(capsys):
  menu.print_video_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Play the "Why Join InCollege?" video
----------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu
'''
def test_print_search_for_user_menu(capsys):
  menu.print_search_for_user_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Search for an active InCollege user
-------------------------------------
What do you want to do?
1. Continue
2. Return to Start Menu
'''
  
def test_print_find_someone_you_know_menu(capsys):
  menu.print_find_someone_you_know_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Find someone you know
-----------------------
What do you want to do?
1. Continue
2. Return to Top-level Menu
'''

def test_print_learn_web_dev_menu(capsys):
  menu.print_learn_web_dev_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Learn Web Development
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu
'''

def test_print_learn_coding_menu(capsys):
  menu.print_learn_coding_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Learn Coding
------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu
'''

def test_print_learn_communication_menu(capsys):
  menu.print_learn_communication_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Learn Communication
-------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu
'''
def test_print_learn_resume_critique_menu(capsys):
  menu.print_learn_resume_critique_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Learn Resume Critique
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu
'''
  
def test_print_learn_excel_menu(capsys):
  menu.print_learn_excel_menu()
  stdout, stderr = capsys.readouterr()
  assert stdout == '''
Learn Microsoft Excel
---------------------
What do you want to do?
1. Continue
2. Return to the Learn a Skill Menu
'''
