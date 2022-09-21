import database as db
import login
import menu
import src.pages.job_search_page as job_search_page
import src.constants.student_success_story as story

loggedInUser = ""


def goto_start_menu_state():

    print(story.STUDENT_SUCCESS_STORY)

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

    print("\nLogin:")
    username = input("Username: ")
    password = input("Password: ")

    if not db.user_exists_in_db(username, password):
        print("Incorrect username/password, please try again.")
        goto_logging_in_state()
        return

    print("\nYou have successfully logged in.")
    global loggedInUser
    loggedInUser = username
    goto_logged_in_state()


def goto_logged_in_state():

    menu.print_top_level_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_find_job(user_input):
        job_search_page.display_job_search_page()

    elif menu.user_chose_to_find_someone(user_input):
        print("\nUnder Construction.")

    elif menu.user_chose_to_learn_a_skill(user_input):
        goto_learn_a_skill_state()


def goto_learn_a_skill_state():
    menu.print_skills_menu()
    user_input = input("\nEnter a selection: ")

    if menu.user_chose_to_learn_web_dev(user_input):
        print("\nUnder construction.")

    elif menu.user_chose_to_learn_coding(user_input):
        print("\nUnder construction.")

    elif menu.user_chose_to_learn_communication(user_input):
        print("\nUnder construction.")

    elif menu.user_chose_to_learn_resume_critique(user_input):
        print("\nUnder construction.")

    elif menu.user_chose_to_learn_excel(user_input):
        print("\nUnder construction.")

    elif menu.user_chose_to_goto_top_level_menu(user_input):
        goto_logged_in_state()


def goto_create_new_account_state():

    print("\nCreate a new user:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not db.can_add_more_users():
        print(
            "All permitted accounts have been created, please come back later."
        )
        return

    elif not login.username_is_unique(username, db.get_database()):
        print("That username is not available.")
        return

    elif login.password_is_too_short(password):
        print("Password is too short.")
        return

    elif login.password_is_too_long(password):
        print("Password is too long.")
        return

    elif not login.password_contains_uppercase_letter(password):
        print('Password must have at least one uppercase letter.')
        return

    elif not login.password_contains_number(password):
        print("Password must have at least one numeral.")
        return

    elif not login.password_contains_special_char(password):
        print("Password must have atleast one special character.")
        return

    db.add_user_to_db(first_name, last_name, username, password)
    print("Account successfully created.")
    goto_start_menu_state()
