import state
import menu
import pytest
import unittest.mock as mock


def test_start_menu(capsys):
    menu.print_start_menu()
    stdout, stderr = capsys.readouterr()
    assert stdout == '''
InCollege
---------
1. Login
2. Sign up
'''


def test_user_chose_to_create_new_account():
    assert menu.user_chose_to_create_new_account("2") == True
    assert menu.user_chose_to_create_new_account("5") == False
    assert menu.user_chose_to_create_new_account("1") == False

def test_user_chose_to_login():
    assert menu.user_chose_to_login("1") == True
    assert menu.user_chose_to_login("0") == False
    assert menu.user_chose_to_login("test") == False


def test_user_chose_to_find_job():
    assert menu.user_chose_to_find_job("1") == True
    assert menu.user_chose_to_find_job("0") == False
    assert menu.user_chose_to_find_job("test") == False


def test_user_chose_to_find_someone():
    assert menu.user_chose_to_find_someone("2") == True
    assert menu.user_chose_to_find_someone("0") == False
    assert menu.user_chose_to_find_someone("test") == False


def test_user_chose_to_learn_a_skill():
    assert menu.user_chose_to_learn_a_skill("3") == True
    assert menu.user_chose_to_learn_a_skill("0") == False
    assert menu.user_chose_to_learn_a_skill("test") == False


def test_user_chose_to_learn_web_dev():
    assert menu.user_chose_to_learn_web_dev("1") == True
    assert menu.user_chose_to_learn_web_dev("0") == False
    assert menu.user_chose_to_learn_web_dev("test") == False


def test_user_chose_to_learn_coding():
    assert menu.user_chose_to_learn_coding("2") == True
    assert menu.user_chose_to_learn_coding("0") == False
    assert menu.user_chose_to_learn_coding("test") == False


def test_user_chose_to_learn_communication():
    assert menu.user_chose_to_learn_communication("3") == True
    assert menu.user_chose_to_learn_communication("0") == False
    assert menu.user_chose_to_learn_communication("test") == False


def test_user_chose_to_learn_resume_critique():
    assert menu.user_chose_to_learn_resume_critique("4") == True
    assert menu.user_chose_to_learn_resume_critique("0") == False
    assert menu.user_chose_to_learn_resume_critique("test") == False


def test_user_chose_to_learn_excel():
    assert menu.user_chose_to_learn_excel("5") == True
    assert menu.user_chose_to_learn_excel("0") == False
    assert menu.user_chose_to_learn_excel("test") == False


def test_user_chose_to_goto_top_level_menu():
    assert menu.user_chose_to_goto_top_level_menu("6") == True
    assert menu.user_chose_to_goto_top_level_menu("0") == False
    assert menu.user_chose_to_goto_top_level_menu("test") == False
