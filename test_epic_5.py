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


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_has_profile(get_database_object, update_database_object):
  userController.set_has_profile("naruto", True)
  assert userController.get_user_by_id("1")["has_profile"] == True


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_major(get_database_object, update_database_object):
  userController.set_user_major("naruto", "English")
  assert userController.get_user_by_id("1")["major"] == "English"


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_university(get_database_object, update_database_object):
  userController.set_user_university("naruto", "UCF")
  assert userController.get_user_by_id("1")["university"] == "UCF"

  