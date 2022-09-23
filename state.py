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

    if user_input == "1":
        return goto_logging_in_state()

    elif user_input == "2":
        return goto_create_new_account_state()

    elif user_input == "3":
        return goto_watch_video_state()

    elif user_input == "4":
        return goto_search_for_user_state()

    elif user_input == "5":
        quit()

    else:
        print("Invalid selection. Please try again.")
        return goto_start_menu_state()


def goto_logging_in_state():

    print("\nLogin:")
    username = input("Username: ")
    password = input("Password: ")

    if not db.user_exists_in_db(username, password):
        print("Incorrect username/password, please try again.")
        return goto_logging_in_state()
        

    print("\nYou have successfully logged in.")
    global loggedInUser
    loggedInUser = username
    goto_logged_in_state()


def goto_logged_in_state():

    menu.print_top_level_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        job_search_page.display_job_search_page()

    elif user_input == "2":
        print("\nUnder Construction.")

    elif user_input == "3":
        return goto_learn_a_skill_state()
    
    elif user_input == "4":
        return goto_start_menu_state()


def goto_learn_a_skill_state():
    menu.print_skills_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        print("\nUnder construction.")

    elif user_input == "2":
        print("\nUnder construction.")

    elif user_input == "3":
        print("\nUnder construction.")

    elif user_input == "4":
        print("\nUnder construction.")

    elif user_input == "5":
        print("\nUnder construction.")

    elif user_input == "6":
        return goto_logged_in_state()


def goto_create_new_account_state():

    print("\nCreate a new user:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not db.can_add_more_users():
        print("All permitted accounts have been created, please come back later.")        
        return goto_start_menu_state()

    elif not login.username_is_unique(username, db.get_database()):
        print("That username is not available.")        
        return goto_start_menu_state()

    elif login.password_is_too_short(password):
        print("Password is too short.")    
        return goto_start_menu_state()

    elif login.password_is_too_long(password):
        print("Password is too long.")        
        return goto_start_menu_state()

    elif not login.password_contains_uppercase_letter(password):
        print('Password must have at least one uppercase letter.')        
        return goto_start_menu_state()

    elif not login.password_contains_number(password):
        print("Password must have at least one numeral.")        
        return goto_start_menu_state()

    elif not login.password_contains_special_char(password):
        print("Password must have atleast one special character.")        
        return goto_start_menu_state()

    db.add_user_to_db(first_name, last_name, username, password)
    print("Account successfully created.")
    goto_start_menu_state()

def goto_watch_video_state():            
    menu.print_video_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_start_menu_state()

    else:
        print("Invalid selection.")
        return goto_watch_video_state()

    print("Video is now playing.")
    return goto_watch_video_state()

def goto_search_for_user_state():   
    menu.print_search_for_user_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass
        
    elif user_input == "2":
        return goto_start_menu_state()

    else:
        print("Invalid selection. Please try again.")
        return goto_search_for_user_state()

    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    if db.name_found_in_db(first_name, last_name):
        print("\nThey are a part of the InCollege system.")
        return goto_start_menu_state()

    else:
        print("\nThey are not yet a part of the InCollege system.")
        return goto_search_for_user_state()

def goto_find_someone_you_know_state():
    menu.print_find_someone_you_know_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_logged_in_state()

    else:
        print("Invalid selection")
        return goto_find_someone_you_know_state()
    
    print("\nUnder Construction.")
    goto_find_someone_you_know_state()

def goto_learn_web_dev_state():
    menu.print_learn_web_dev_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_learn_a_skill_state()

    else:
        print("Invalid selection")
        return goto_learn_web_dev_state()

    print("\nUnder Construction.")
    return goto_learn_web_dev_state()

def goto_learn_coding_state():
    menu.print_learn_coding_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_learn_a_skill_state()

    else:
        print("Invalid selection")
        return goto_learn_coding_state()

    print("\nUnder Construction.")
    return goto_learn_web_dev_state()

def goto_learn_communication_state():
    menu.print_learn_communication_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_learn_a_skill_state()

    else:
        print("Invalid selection")
        return goto_learn_communication_state()

    print("\nUnder Construction.")
    return goto_learn_communication_state()

def goto_learn_resume_critique_state():
    menu.print_learn_resume_critique_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_learn_a_skill_state()

    else:
        print("Invalid selection")
        return goto_learn_resume_critique_state()

    print("\nUnder Construction.")
    return goto_learn_resume_critique_state()

def goto_learn_excel_state():
    menu.print_learn_excel_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return goto_learn_a_skill_state()

    else:
        print("Invalid selection")
        return goto_learn_excel_state()

    print("\nUnder Construction.")
    return goto_learn_excel_state()
