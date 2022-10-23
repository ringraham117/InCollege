import json


def get_mock_user_data():
    return {
        "users": [{
            "username": "naruto",
            "unique_id": "1",
            "password": "Password1@",
            "first_name": "Naruto",
            "last_name": "Uzumaki",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": ['1', '2', '3'],
            "friend_requests": ['4'],
            "active_profile": False,
            "title": "",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about": "",
            "education": "",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "sasuke",
            "unique_id": "2",
            "password": "Password1@",
            "first_name": "Sasuke",
            "last_name": "Uchiha",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": ['1'],
            "friend_requests": [],
            "active_profile": False,
            "title": "Comp sci student",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            " I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "Community College",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "sakura",
            "unique_id": "3",
            "password": "Password1@",
            "first_name": "Sakura",
            "last_name": "Haruno",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": ['1'],
            "friend_requests": [],
            "active_profile": True,
            "title": "Sakura Haruno - Profile",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            "I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "High School",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "kakashi",
            "unique_id": "4",
            "password": "Password1@",
            "first_name": "Kakashi",
            "last_name": "Hatake",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": ['1'],
            "friend_requests": [],
            "active_profile": True,
            "title": "Kakashi Hatake - Profile",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            "I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "High School",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "shikamaru",
            "unique_id": "5",
            "password": "Password1@",
            "first_name": "Shikamaru",
            "last_name": "Nara",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": [],
            "friend_requests": [],
            "active_profile": True,
            "title": "Shikamaru Nara - Profile",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            "I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "High School",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "hinata",
            "unique_id": "6",
            "password": "Password1@",
            "first_name": "Hinata",
            "last_name": "Hyuga",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": [],
            "friend_requests": [],
            "active_profile": True,
            "title": "Hinata Hyuga - Profile",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            "I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "High School",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }, {
            "username": "lee",
            "unique_id": "7",
            "password": "Password1@",
            "first_name": "Lee",
            "last_name": "Ryuga",
            "language": "English",
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "friends": [],
            "friend_requests": [],
            "active_profile": True,
            "title": "Lee Ryuga - Profile",
            "university": "University of South Florida",
            "major": "Computer Science",
            "about":
            "I am a computer science student at USF. I am looking for a roommate to share an apartment with.",
            "education": "High School",
            "experience": [
                {},
                {},
                {}
            ],
            "school": "",
            "degree": "",
            "years": ""
        }]
    }


def get_mock_unique_id_data():
    return {"unique_id": 8}


def update_user_credentials_object():
    database_file = open('databases/user_credentials.json', 'w')
    json.dump(get_mock_user_data(), database_file, indent=2)


def update_unique_id_object():
    database_file = open('databases/unique_id.json', 'w')
    json.dump(get_mock_unique_id_data(), database_file, indent=2)


update_user_credentials_object()
update_unique_id_object()
