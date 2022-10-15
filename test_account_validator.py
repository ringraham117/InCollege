import src.account_validator as account_validator
import src.user_database_controller as user_db

def test_username_is_unique():
    user_db.clear_users_list()
    assert account_validator.username_is_unique("user1", user_db.get_users_list()) == True

    user_db.add_user_to_db("Mel", "Gibson", "user1", "password")
    assert account_validator.username_is_unique("user1", user_db.get_users_list()) == False

def test_password_is_too_short():
    assert account_validator.password_is_too_short("abc")== True
    assert account_validator.password_is_too_short("Validpas1!")== False

def test_password_is_too_long():
    assert account_validator.password_is_too_long("abcdefghijklmnop")== True
    assert account_validator.password_is_too_long("Validpas1!")== False

def test_password_contains_uppercase_letter():
    assert account_validator.password_contains_uppercase_letter("abcdefghi") == False
    assert account_validator.password_contains_uppercase_letter("Validpas1!") == True

def test_password_contains_number():
    assert account_validator.password_contains_number("abcdefghi") == False
    assert account_validator.password_contains_number("Validpas1!") == True

def test_password_contains_special_char():
    assert account_validator.password_contains_special_char("abcdefghi") == False
    assert account_validator.password_contains_special_char("Validpas1!") == True

