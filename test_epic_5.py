import pytest
from unittest import mock

import src.services.user_controller as userController
import src.shared.password_validator as passwordValidator
import src.services.job_controller as jobController
import src.models.job_model as jobModel
import src.models.user_model as userModel

# note: I'm importing routes here instead of the actual module in screens because if I do, it results in a circular import error
import src.routing.routes as routes
import development.create_mock_user_data as mock_data

mock_user = {
  "users": [{
    "unique_id": "1",
    "username": "naruto",
    "password": "Password1@",
    "title": "",
    "first_name": "Naruto",
    "last_name": "Uzumaki",
    "language": "English",
    "university": "USF",
    "major": "CSE",
    "sms_notifications": False,
    "email_notifications": False,
    "ad_notifications": False,
    "friends": ['2', '3'],
    "friend_requests": [''],
    "about": "I am a ninja",
    "has_profile": False
  }]
}


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_title(get_database_object, update_database_object):
  userController.set_user_title("naruto", "Computer Science Student")
  assert userController.get_user_by_id(
    "1")["title"] == "Computer Science Student"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_about(get_database_object, update_database_object):
  userController.set_user_about("naruto", "I am a computer science student")
  assert userController.get_user_by_id(
    "1")["about"] == "I am a computer science student"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_has_profile(get_database_object, update_database_object):
  userController.set_has_profile("naruto", True)
  assert userController.get_user_by_id("1")["has_profile"] == True


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_major(get_database_object, update_database_object):
  userController.set_user_major("naruto", "English")
  assert userController.get_user_by_id("1")["major"] == "English"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_university(get_database_object, update_database_object):
  userController.set_user_university("naruto", "UCF")
  assert userController.get_user_by_id("1")["university"] == "UCF"


# Test Function
@mock.patch('src.routing.routes.userhomeScreen.handle_user_selection')
@mock.patch('src.routing.routes.userhomeScreen.handle_friend_requests')
def test_user_create_profile_option(handle_user_selection_mock, handle_friend_requests_mock, capsys, monkeypatch):
  routes.userhomeScreen.auth.logged_in_user = mock_user['users'][0]
  handle_user_selection_mock.return_value = None
  handle_friend_requests_mock.return_value = None
  monkeypatch.setattr('builtins.input', lambda selection: '', raising=False)
  routes.userhomeScreen.screen()
  stdout, stderr = capsys.readouterr()
  assert "5 - Create Profile" in stdout
  assert routes.screenNames.CREATE_PROFILE_SCREEN in routes.userhomeScreen.screen_options
  assert routes.userhomeScreen.screen_exists("Create Profile") == True


# Test Function
@mock.patch('src.routing.routes.createprofileScreen.handle_user_selection')
def test_user_show_profile_option(handle_user_selection_mock, capsys,
                                  monkeypatch):
  user = mock_data.get_mock_user_data()['users'][0]
  user['has_profile'] = True
  routes.createprofileScreen.auth.logged_in_user = user
  handle_user_selection_mock.return_value = None
  monkeypatch.setattr('builtins.input', lambda selection: '', raising=False)
  routes.createprofileScreen.screen()
  stdout, stderr = capsys.readouterr()
  assert stdout.startswith(
    f"\n\x1b[94mThis is the profile of {user['first_name']} {user['last_name']}!"
  )
  assert "Title" and "University" and "Major" and "About" and "Experience" and "Education" in stdout


# Test Function
@mock.patch(
  'src.routing.routes.createprofileScreen.user_selects_to_continue_profile_creation'
)
@mock.patch('src.routing.routes.createprofileScreen.past_job_limit_reached')
@mock.patch(
  'src.routing.routes.createprofileScreen.user_selected_to_enter_past_job')
def test_enter_profile_information(
    user_selects_to_continue_profile_creation_mock,
    past_job_limit_reached_mock, user_selected_to_enter_past_job_mock, capsys,
    monkeypatch):
  routes.createprofileScreen.auth.logged_in_user = mock_user['users'][0]

  user_selects_to_continue_profile_creation_mock.return_value = False

  inputs = iter([
    'Hokage',
    "I was the best ninja in the hidden leaf village but now i go to usf",
    'university of south florida', 'computer science', '2019 - 2023'
  ])
  monkeypatch.setattr('builtins.input', lambda selection: next(inputs))
  title, about, job, school, degree, years = routes.createprofileScreen.get_user_profile_data(
  )

  assert title == "Hokage"
  assert about == "I was the best ninja in the hidden leaf village but now i go to usf"
  assert school == "University Of South Florida"
  assert degree == "Computer Science"
  assert years == '2019 - 2023'


# Test Function
def test_profile_contains_proper_information(monkeypatch):
  user = mock_data.get_mock_user_data()['users'][0]
  assert user.get('education') != None
  assert user.get('experience') != None
  assert user.get('degree') != None
  assert user.get('school') != None
  assert user.get('years') != None


# should I also test db functionality to see if the db is updated with the correct info as well?
# Test Function
def test_enter_job_information(monkeypatch):
  inputs = iter([
    'Hokage', 'Land of Fire', '??/??/??', '??/??/??', 'Hidden Leaf Village',
    'Leader of the village'
  ])
  monkeypatch.setattr('builtins.input', lambda input: next(inputs))
  title, employer, start_date, end_date, location, description = routes.createprofileScreen.read_past_job_details(
  )
  assert title == 'Hokage'
  assert employer == 'Land of Fire'
  assert start_date == '??/??/??'
  assert end_date == '??/??/??'
  assert location == 'Hidden Leaf Village'
  assert description == 'Leader of the village'


# Test Function
def test_set_past_job_title():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the title of Past Job #1
  userController.set_past_job_title("user", 0, "My Dream Job")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["job_title"] == "My Dream Job"


# Test Function
def test_set_past_job_employer():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the employer of Past Job #1
  userController.set_past_job_employer("user", 0, "My Dream Employer")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["job_employer"] == "My Dream Employer"


# Test Function
def test_set_past_job_start_date():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the start date of Past Job #1
  userController.set_past_job_start_date("user", 0, "800 BC")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["start_date"] == "800 BC"


# Test Function
def test_set_past_job_end_date():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the end date of Past Job #1
  userController.set_past_job_end_date("user", 0, "January 1st, 2076")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["end_date"] == "January 1st, 2076"


# Test Function
def test_set_past_job_location():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the location of Past Job #1
  userController.set_past_job_location("user", 0, "Hidden Leaf Village")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["end_date"] == "Hidden Leaf Village"


# Test Function
def test_set_past_job_location():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the location of Past Job #1
  userController.set_past_job_location("user", 0, "Hidden Leaf Village")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1["location"] == "Hidden Leaf Village"


# Test Function
def test_set_past_job_description():

  # Clear the user list
  userController.clear_users_list()

  # Check that more users can be added
  assert userController.is_database_limit_reached() == False

  # Add 1 user to the database
  new_user = userModel.User("1", "user", "password", "April", "May", "USF",
                            "CompSci")
  userController.add_user(new_user)

  # Set the description of Past Job #1
  userController.set_past_job_description(
    "user", 0, "Wonderful. Couldn't be better! Tremendous!")

  test_user = userController.get_user_by_username("user")
  past_job_list = test_user["experience"]
  past_job_1 = past_job_list[0]

  assert past_job_1[
    "description"] == "Wonderful. Couldn't be better! Tremendous!"
