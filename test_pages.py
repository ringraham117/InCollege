import src.user_database_controller as user_db
import src.state as state


#EPIC - 3 TEST
def test_about_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "3", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_blog_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "5", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

Under construction!

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_browse_incollege(capsys, monkeypatch):

    inputs = iter(["5", "2", "0", "0", "7"])

    # Simulate entering those values into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Start the app
    state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

Under construction!

0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_business_solutions_page(capsys, monkeypatch):
  inputs = iter(["5", "3", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page
Under construction!

0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

# #EPIC - 3 TEST
def test_careers_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "6", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

Under construction!

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_copyright_notice_page(capsys, monkeypatch):
  inputs = iter(["6", "1", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

In College Pressroom: Stay on top of the latest news, updates, and reports

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_developers_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "7", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

Under construction!

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_directories_page(capsys, monkeypatch):
  inputs = iter(["5", "4", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page
Under construction!

0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

#EPIC - 3 TEST
def test_help_center_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "2", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

We are here to help!

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

# EPIC 3 - Test
def test_language_settings(monkeypatch):
  
  # Clear the users list
  user_db.clear_users_list()

  # Add in a new user
  user_db.add_user_to_db("Tom", "Brady", "Tom", "password")
  users_list = user_db.get_users_list()
  test_user = users_list[0]

  # Check that the language setting is English
  assert test_user["language"] == "English"

  # Update the language setting to Spanish
  # List out inputs to simulate
  inputs = iter(["1", "Tom", "password", "5", "10", "2", "0", "6", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

  # Check that the language setting is Spanish
  users_list = user_db.get_users_list()
  test_user = users_list[0]
  assert test_user["language"] == "Spanish"

#EPIC - 3 TEST
def test_press_page(capsys, monkeypatch):
  inputs = iter(["5", "1", "4", "0", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the app
  state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

In College Pressroom: Stay on top of the latest news, updates, and reports

0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

# EPIC 3 - Test
def test_useful_links_general_sign_up(capsys, monkeypatch):
    
    user_db.clear_users_list()
    
    inputs = iter(["5", "1", "1", "first", "last", "user1", "Password1!", "7"])

    # Simulate entering those values into the terminal
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Start the app
    state.show_start_menu_page()

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
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

1 - General
2 - Browse InCollege
3 - Business Solutions
4 - Directories
0 - Previous Page

1 - Sign Up
2 - Help Center
3 - About
4 - Press
5 - Blog
6 - Careers
7 - Developers
0 - Previous Page

Create a new user:
Account successfully created.


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

Welcome to InCollege
--------------------
1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit

Program is exiting!
'''

# EPIC 3 - Test
def test_user_agreement_page(capsys, monkeypatch):
  inputs = iter(["6", "4", "0", "0", "7"])

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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
By using InCollege you agree to abide by the terms and conditions listed below. If you violate these rules, then we reserve the right to suspend your account. 
Platform Rules:
- The use of our platform should be related to professional networking. This is not a general forum
- No NSFW content
  - Discrimination based on ethnicity, religion, or political opinions will not be tolerated

0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''

# EPIC 3 - Test
def test_cookie_policy_page(capsys, monkeypatch):
  inputs = iter(["6", "6", "0", "0", "7"])

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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
InCollege uses cookies to enhance the user experience in the application. This includes basic information on your current session and the pages you navigate to while logged in. Additional cookies are used for targeted advertising, bringing you ads that you would like to see. These may track your browsing on other sites. To turn off targeted advertising, navigate to InCollege Important Links -> Guest Controls then select Targeted Ads to toggle on or off, these are on by default

0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''

# EPIC 3 - Test
def test_privacy_policy_page(capsys, monkeypatch):
  inputs = iter(["6", "5", "0", "0", "7"])

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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
InCollege will not sell your data to any 3rd parties.
Only the necessary data related to your account will be used when fulfilling site requests.
The data we store and use includes: 
- Username
- Password Hash
- First Name
- Last Name
- Language
- Guest Controls
  - SMS
  - Email
  - Targeted Ads

1 - Guest Controls
0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''

# EPIC 3 - Test
def test_links_before_login(capsys, monkeypatch):
  inputs = iter(["7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the control flow
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

# EPIC 3 - Test
def test_brand_policy_page(capsys, monkeypatch):
  inputs = iter(["6", "8", "0", "0", "7"])

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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
InCollege users may only use InCollege trademarks in strict accordance with this policy. InCollege trademarks may be used on commercial merchandise and online only by persons and entities licensed by InCollege. InCollege should be consulted whenever it is not clear whether a proposed use is permissible. Any unauthorized use of the brand is prohibited.

0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''

# EPIC 3 - Test
def test_accessibility_page(capsys, monkeypatch):
  inputs = iter(["6", "3", "0", "0", "7"])

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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
You may use this app for purposes of meeting others who are in college. Through the app, you may perform functions such as connecting with other users, finding a job, learning skills, etc. From time to time this app may be updated to provide other features and functionality. Any unauthorized use of this app is prohibited

0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''


# EPIC 3 - Test
def test_links_after_login(capsys, monkeypatch):
 
  # Clears the list of users
  db.clear_users_list()
  
  # Adds a user to the database
  db.add_user_to_db("first", "last", "user", "password")

  inputs = iter(["1", "user", "password", "6", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the control flow
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

# EPIC 3 - Test
def test_copyright_policy_page(capsys, monkeypatch):
  
  # Lists inputs to be simulated
  inputs = iter(["6", "7", "0", "0", "7"])

  # Simulate entering those values into the terminal
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Start the control flow
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


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page
You may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to InCollege without obtaining the prior written consent of InCollege.

0 - Previous Page


1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement
5 - Privacy Policy
6 - Cookie Policy
7 - Copyright Policy
8 - Brand Policy
9 - Guest Controls
10 - Language Settings
0 - Previous Page


I found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.
Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.
This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Mark Zuckerberg

1 - Login
2 - Sign Up
3 - Play video ("Why Join InCollege?")
4 - Search for InCollege users
5 - Useful Links
6 - InCollege Important Links
7 - Exit
0 - Previous Page
'''
