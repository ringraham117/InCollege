import login
import database as db

def test_username_is_unique():
    db.clear_db()
    assert login.username_is_unique("user1", db.get_users_list()) == True

    db.add_user_to_db("Mel", "Gibson", "user1", "password")
    assert login.username_is_unique("user1", db.get_users_list()) == False

def test_password_is_too_short():
    assert login.password_is_too_short("abc")== True
    assert login.password_is_too_short("Validpas1!")== False

def test_password_is_too_long():
    assert login.password_is_too_long("abcdefghijklmnop")== True
    assert login.password_is_too_long("Validpas1!")== False

def test_password_contains_uppercase_letter():
    assert login.password_contains_uppercase_letter("abcdefghi") == False
    assert login.password_contains_uppercase_letter("Validpas1!") == True

def test_password_contains_number():
    assert login.password_contains_number("abcdefghi") == False
    assert login.password_contains_number("Validpas1!") == True

def test_password_contains_special_char():
    assert login.password_contains_special_char("abcdefghi") == False
    assert login.password_contains_special_char("Validpas1!") == True

