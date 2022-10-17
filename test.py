import pytest
from unittest import mock
import src.services.user_controller as userController
import src.shared.password_validator as passwordValidator
import src.services.job_controller as jobController
import src.models.job_model as jobModel

mock_user = {
  "users": [{
    "unique_id": "1",
    "username": "naruto",
    "password": "Password1@",
    "first_name": "Naruto",
    "last_name": "Uzumaki",
    "language": "English",
    "university": "USF",
    "major": "CSE",
    "sms_notifications": False,
    "email_notifications": False,
    "ad_notifications": False,
    "friends": ['2', '3'],
    "friend_requests": ['']
  }]
}


#epic 1 already has this(did not add)
# @pytest.mark.parametrize("password, expected_password", [
#   pytest.param("password", False, id='Missing Upper case, Special and Number'),
#   pytest.param("Password", False, id='Missing Special and Number'),
#   pytest.param("Password1", False, id='Missing Special'),
#   pytest.param("Password1@12345", False, id='Long Password'),
#   pytest.param("Pass1@", False, id='Short Password'),
#   pytest.param("Password1@", True, id='Valid Password')
# ])
# def test_is_password_valid(password, expected_password):
#   assert passwordValidator.is_password_valid(password) == expected_password

#added to Epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_id(get_database_object, update_database_object):
  assert userController.get_user_by_username("naruto") == mock_user["users"][0]

# Added to epic 1
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_username(get_database_object, update_database_object):
  assert userController.get_user_by_username("naruto") == mock_user["users"][0]

# Added to epic 2
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_first_name(get_database_object, update_database_object):
  assert userController.get_users_by_first_name("Naruto") == mock_user["users"]


# Added to epic 4 tests
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_last_name(get_database_object, update_database_object):
  assert userController.get_users_by_last_name("Uzumaki") == mock_user["users"]


# Added to epic 4 tests
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_university(get_database_object, update_database_object):
  assert userController.get_users_by_university("USF") == mock_user["users"]

#added to Epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_major(get_database_object, update_database_object):
  assert userController.get_users_by_major("CSE") == mock_user["users"]

#added to Epic 2
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_first_last_name(get_database_object,
                                     update_database_object):
  assert userController.get_user_by_first_last_name(
    "Naruto", "Uzumaki") == mock_user["users"][0]

#added to epic 3
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_set_user_language(get_database_object,
                                    update_database_object):
  userController.set_user_language("1", "Spanish")
  assert userController.get_user_by_id("1")["language"] == "Spanish"

#added to epic 3
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_sms(get_database_object, update_database_object):
  userController.set_user_sms("1", True)
  assert userController.get_user_by_id("1")["sms_notifications"] == True

# added to epic 3
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_email(get_database_object, update_database_object):
  userController.set_user_email("1", True)
  assert userController.get_user_by_id("1")["email_notifications"] == True

#added to epic 3
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_ads(get_database_object, update_database_object):
  userController.set_user_ads("1", True)
  assert userController.get_user_by_id("1")["ad_notifications"] == True


# Added to epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_friend_requests(get_database_object, update_database_object):
  assert userController.get_user_friend_requests("1") == ['']

  
# Added to epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_friends(get_database_object, update_database_object):
  assert userController.get_user_friends("1") == ['2', '3']


# Added to epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_add_user_to_friends(get_database_object, update_database_object):
  userController.add_user_to_friends("1", "4")
  assert userController.get_user_friends("1") == ['2', '3', '4']


# Added to epic 4
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_delete_user_friend(get_database_object, update_database_object):
  userController.delete_user_friend("1", "3")
  assert userController.get_user_friends("1") == ['2', '4']


#-------------------Job Controller Tests-------------------#
#added to epic 2
mock_job = {
  "jobs": [{
    "user": "Naruto",
    "title": "Software Engineer",
    "description": "Software Engineer",
    "employer": "Google",
    "location": "Mountain View, CA",
    "requirements": "CSE",
    "salary": "100000",
  }]
}


@mock.patch.object(jobController, 'get_database_object', return_value=mock_job)
@mock.patch.object(jobController,
                   'update_database_object',
                   return_value="Success")
def test_add_job(get_database_object, update_database_object):
  job = jobModel.Job("Naruto", "Software Engineer", "Google",
                     "Mountain View, CA", "CSE", "100000")
  jobController.add_job(job)
  assert len(mock_job["jobs"]) == 2


#-------------------Router Test-------------------#
