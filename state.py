import database as db
import login
import menu


def goto_start_menu_state():

    menu.print_start_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_login(user_input):
        goto_logging_in_state()

    elif menu.user_chose_to_create_new_account(user_input):
        goto_create_new_account_state()

    else:
        print("Invalid selection. Please try again.")
        goto_start_menu_state()

def goto_logging_in_state():

    print("\n\nLogin:")
    username = input("Username: ")
    password = input("Password: ")

    if not db.user_exists_in_db(username, password):
        print("\nIncorrect username/password, please try again.")
        goto_logging_in_state()

    print("\nYou have successfully logged in.")
    goto_logged_in_state()


def goto_logged_in_state():

    menu.print_top_level_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_find_job(user_input):
        print("\nUnder construction.")
        goto_logged_in_state()

    elif menu.user_chose_to_find_someone(user_input):
        print("\nUnder construction.")
        goto_logged_in_state()

    elif menu.user_chose_to_learn_a_skill(user_input):
        goto_learn_a_skill_state()

    else:
        print("\nInvalid selection.")
        goto_logged_in_state()


def goto_learn_a_skill_state():
    menu.print_skills_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_learn_web_dev(user_input):
        print("\nUnder construction.")
        goto_learn_a_skill_state()

    elif menu.user_chose_to_learn_coding(user_input):
        print("\nUnder construction.")
        goto_learn_a_skill_state()

    elif menu.user_chose_to_learn_communication(user_input):
        print("\nUnder construction.")
        goto_learn_a_skill_state()

    elif menu.user_chose_to_learn_resume_critique(user_input):
        print("\nUnder construction.")
        goto_learn_a_skill_state()
    
    elif menu.user_chose_to_learn_excel(user_input):
        print("\nUnder construction.")
        goto_learn_a_skill_state()

    elif menu.user_chose_to_goto_top_level_menu(user_input):
        goto_logged_in_state()        

    else:
        print("\nInvalid selection")
        goto_learn_a_skill_state()

def goto_create_new_account_state():

    print("\nCreate a new user:")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not db.can_add_more_users():
        print("All permitted accounts have been created, please come back later.")
        goto_create_new_account_state()

    elif not login.username_is_unique(username):
        print("That username is not available.")
        goto_create_new_account_state()

    elif login.password_is_too_short(password):
        print("Password is too short.")
        goto_create_new_account_state()

    elif login.password_is_too_long(password):
        print("Password is too long.")
        goto_create_new_account_state()

    elif not login.password_contains_uppercase_letter(password):
        print('Password must have at least one uppercase letter.')
        goto_create_new_account_state()

    elif not login.password_contains_number(password):
        print("Password must have at least one numeral.")
        goto_create_new_account_state()

    elif not login.password_contains_special_char(password):
        print("Password must have atleast one special character.")
        goto_create_new_account_state()

    db.add_user_to_db(username, password)
    print("Account successfully created.")
    goto_start_menu_state()