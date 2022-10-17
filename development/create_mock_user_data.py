import json


def get_mock_user_data():
  return {
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
      "friend_requests": ['4']
    }, {
      "unique_id": "2",
      "username": "sasuke",
      "password": "Password1@",
      "first_name": "Sasuke",
      "last_name": "Uchiha",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": ['1', '3'],
      "friend_requests": []
    }, {
      "unique_id": "3",
      "username": "sakura",
      "password": "Password1@",
      "first_name": "Sakura",
      "last_name": "Haruno",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": ['1', '2'],
      "friend_requests": []
    }, {
      "unique_id": "4",
      "username": "kakashi",
      "password": "Password1@",
      "first_name": "Kakashi",
      "last_name": "Hatake",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": [],
      "friend_requests": []
    }, {
      "unique_id": "5",
      "username": "minato",
      "password": "Password1@",
      "first_name": "Minato",
      "last_name": "Namikaze",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": [],
      "friend_requests": []
    }, {
      "unique_id": "6",
      "username": "itachi",
      "password": "Password1@",
      "first_name": "Itachi",
      "last_name": "Uchiha",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": [],
      "friend_requests": []
    }, {
      "unique_id": "7",
      "username": "shikamaru",
      "password": "Password1@",
      "first_name": "Shikamaru",
      "last_name": "Nara",
      "language": "English",
      "university": "USF",
      "major": "CSE",
      "sms_notifications": False,
      "email_notifications": False,
      "ad_notifications": False,
      "friends": [],
      "friend_requests": []
    }]
  }


def get_mock_unique_id_data():
<<<<<<< HEAD
  return {"unique_id": 8}
=======
  return {"id": 8}
>>>>>>> cd0ecb177e0a260ee6cc0d43f8e32eaae926613d


def update_user_credentials_object():
  database_file = open('databases/user_credentials.json', 'w')
  json.dump(get_mock_user_data(), database_file, indent=2)


def update_unique_id_object():
  database_file = open('databases/unique_id.json', 'w')
  json.dump(get_mock_unique_id_data(), database_file, indent=2)


update_user_credentials_object()
update_unique_id_object()
