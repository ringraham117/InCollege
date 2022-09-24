import state
import menu
import pytest
import unittest.mock as mock


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