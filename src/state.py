import src.account_validator as account_validator
import src.menu as menu
import src.constants.pages as pages
import src.constants.student_success_story as story
import src.job_database_controller as job_db
import src.page_history as page_history
import src.user_database_controller as user_db


def show_about_page(active_user):
    print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_about_page(active_user)

def show_ask_to_join_page():
    menu.print_ask_to_join_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_logging_in_page()

    elif user_input == "2":
        return show_create_new_account_page()

    elif user_input == "3":
        return show_start_menu_page()

    else:
        print("Invalid input.")
        return show_ask_to_join_page()

def show_blog_page(active_user):
    print("\nUnder construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_blog_page(active_user)

def show_browse_incollege_page(active_user):
    print("\nUnder construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_browse_incollege_page(active_user)
  
def show_business_solutions_page(active_user):
    print("Under construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_business_solutions_page(active_user)  

def show_careers_page(active_user):
    print("\nUnder construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_careers_page(active_user)

def show_copyright_notice_page(active_user):
    print("The InCollege name and branding are protected under Copyright")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_important_links_page(active_user)

    else:
        print("Invalid selection")
        return show_copyright_notice_page(active_user)

def show_copyright_policy_page(active_user):
    print("You may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to InCollege without obtaining the prior written consent of InCollege.")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_important_links_page(active_user)

    else:
        print("Invalid selection")
        return show_copyright_policy_page(active_user)

def show_create_new_account_page():

    print("\nCreate a new user:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not user_db.can_add_more_users():
        print("All permitted accounts have been created, please come back later.")
        return show_start_menu_page()

    elif not account_validator.username_is_unique(username, user_db.get_users_list()):
        print("That username is not available.")
        return show_start_menu_page()

    elif account_validator.password_is_too_short(password):
        print("Password is too short.")
        return show_start_menu_page()

    elif account_validator.password_is_too_long(password):
        print("Password is too long.")
        return show_start_menu_page()

    elif not account_validator.password_contains_uppercase_letter(password):
        print('Password must have at least one uppercase letter.')
        return show_start_menu_page()

    elif not account_validator.password_contains_number(password):
        print("Password must have at least one numeral.")
        return show_start_menu_page()

    elif not account_validator.password_contains_special_char(password):
        print("Password must have atleast one special character.")
        return show_start_menu_page()

    user_db.add_user_to_db(first_name, last_name, username, password)
    print("Account successfully created.")
    show_start_menu_page()

def show_developers_page(active_user):
    print("\nUnder construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_developers_page()

def show_directories_page(active_user):
    print("Under construction!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_directories_page(active_user)

def show_exit_page():
    print("\nProgram is exiting!")

def show_find_someone_you_know_page():
    menu.print_find_someone_you_know_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_home_page()

    else:
        print("Invalid selection")
        return show_find_someone_you_know_page()

    print("\nUnder Construction.")
    show_find_someone_you_know_page()

def show_general_useful_links_page(active_user):
    menu.print_general_useful_links_menu()

    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_create_new_account_page()

    elif user_input == "2":
        return show_help_center_page(active_user)

    elif user_input == "3":
        return show_about_page(active_user)

    elif user_input == "4":
        return show_press_page(active_user)

    elif user_input == "5":
        return show_blog_page(active_user)

    elif user_input == "6":
        return show_careers_page(active_user)

    elif user_input == "7":
        return show_developers_page(active_user)

    elif user_input == "0":
        return show_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_general_useful_links_page()

def show_guest_controls_page(active_user):
    controls = user_db.get_guest_controls(active_user["username"])
  
    sms = controls['sms']
    email = controls['email']
    ads = controls['targeted_ads']

    menu.generate_menu(
        [
            'SMS - On' if sms else 'SMS - Off', 
            'Email - On' if email else 'Email - Off', 
            'Targeted Ads - On' if ads else 'Targeted Ads - Off'
        ]
    )

    user_selection = input("\nEnter a selection: ")
  
    while (user_selection != "0"):
        if (user_selection == "1"):
            
            # Toggle sms settings
            sms = not sms
        
        elif (user_selection == "2"):
            
            # Toggle email settings
            email = not email
        
        elif (user_selection == "3"):
            
            # Toggle targeted ads settings
            ads = not ads

        menu.generate_menu(
            [
                'SMS - On' if sms else 'SMS - Off', 
                'Email - On' if email else 'Email - Off', 
                'Targeted Ads - On' if ads else 'Targeted Ads - Off'        
            ]
        )

        user_selection = input("\nEnter a selection: ")

    controls = {
        'sms': sms,
        'email': email,
        'targeted_ads': ads,
    }
    
    user_db.write_guest_controls(active_user["username"], controls)
    return show_important_links_page(active_user)

def show_help_center_page(active_user):
    print("\nWe are here to help!")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_help_center_page(active_user)

def show_home_page(active_user):

    menu.print_top_level_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_job_search_page(active_user)

    elif user_input == "2":
        return show_find_someone_you_know_page()

    elif user_input == "3":
        return show_learn_a_skill_page()

    elif user_input == "4":
        page_history.add_page(pages.HOME_PAGE)
        return show_useful_links_page(active_user)

    elif user_input == "5":
        page_history.add_page(pages.HOME_PAGE)
        return show_important_links_page(active_user)

    elif user_input == "6":
        return show_start_menu_page()

    else:
        print("Invalid selection.")
        return show_home_page(active_user)

def show_important_links_page(active_user):
    menu.print_important_links_menu()
    
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_copyright_notice_page(active_user)

    elif user_input == "2":
        return
    
    elif user_input == "3":
        return

    elif user_input == "4":
        return

    elif user_input == "5":
        return

    elif user_input == "6":
        return

    elif user_input == "7":
        return show_copyright_policy_page()

    elif user_input == "8":
        return

    elif user_input == "9":
        if active_user == None:
            print("\nPlease login to access guest controls")
            return show_important_links_page(None)
        
        return show_guest_controls_page(active_user)

    elif user_input == "10":
        return show_languages_page(active_user)

    elif user_input == "0" and page_history.previous_page_is_start_page(): 
        page_history.remove_current_page()
        return show_start_menu_page()

    elif user_input == "0" and page_history.previous_page_is_home_page():
        page_history.remove_current_page()
        return show_home_page(active_user)

    else:
        return

def show_job_post_page(active_user):
    
    if not job_db.can_add_more_jobs():
        print("\nUnable to add more jobs, database limit exceeded")
        return show_job_search_page()

    user = active_user["username"]
    title = input("\nEnter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")

    job_db.add_job_to_db(user, title, description, employer, location, salary)
    print("\nJob Posted Successfully!\n")
    
def show_job_search_page(active_user):
    menu.print_job_search_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_job_post_page(active_user)
    
    elif user_input == "2":
        return show_home_page()

    else:
        print("Invalid selection")
        return show_job_search_page(active_user)

def show_languages_page(active_user):
    # Check if no one is logged in
    if active_user == None:
        print("\nPlease login to change language settings")
        return show_important_links_page(active_user)
    
    # Present the user with options
    print("\n1 - English")
    print("2 - Spanish")
    print("3 - Return to previous screen")

    # Read the user's input
    user_input = input("\nMake a selection: ")
  
    # Handle the user's input
    if user_input == "1":
        language_selection = "English"

    elif user_input == "2":
        language_selection = "Spanish"

    elif user_input == "3":
        return show_important_links_page(active_user)
        
    else:
        print("Invalid selection.")
        return show_languages_page(active_user)

    print("\nLanguage was set to " + language_selection)

    # Get a reference to the list of users
    database = user_db.get_db_as_dictionary()

    # Iterate through each user
    for user in database["users_list"]:
        
        # If the iterator's username matches that of the logged in user
        if user["username"] == active_user["username"]:
            
            # Sets the iterator's language setting based on the language selection
            user["language"] = language_selection

    # Update the database with the updated list of users
    user_db.update_users_list(database)

    # Returns to the previous page (Important links page)
    return show_important_links_page(active_user)

def show_learn_a_skill_page():
    menu.print_skills_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_learn_web_dev_page()

    elif user_input == "2":
        return show_learn_coding_page()

    elif user_input == "3":
        return show_learn_communication_page()

    elif user_input == "4":
        return show_learn_resume_critique_page()

    elif user_input == "5":
        return show_learn_excel_page()

    elif user_input == "6":
        return show_home_page()

def show_learn_coding_page():
    menu.print_learn_coding_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_learn_a_skill_page()

    else:
        print("Invalid selection")
        return show_learn_coding_page()

    print("\nUnder Construction.")
    return show_learn_coding_page()

def show_learn_communication_page():
    menu.print_learn_communication_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_learn_a_skill_page()

    else:
        print("Invalid selection")
        return show_learn_communication_page()

    print("\nUnder Construction.")
    return show_learn_communication_page()

def show_learn_excel_page():
    menu.print_learn_excel_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_learn_a_skill_page()

    else:
        print("Invalid selection")
        return show_learn_excel_page()

    print("\nUnder Construction.")
    return show_learn_excel_page()

def show_learn_resume_critique_page():
    menu.print_learn_resume_critique_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_learn_a_skill_page()

    else:
        print("Invalid selection")
        return show_learn_resume_critique_page()

    print("\nUnder Construction.")
    return show_learn_resume_critique_page()

def show_learn_web_dev_page():
    menu.print_learn_web_dev_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_learn_a_skill_page()

    else:
        print("Invalid selection")
        return show_learn_web_dev_page()

    print("\nUnder Construction.")
    return show_learn_web_dev_page()

def show_login_page():

    print("\nLogin:")
    username = input("Username: ")
    password = input("Password: ")

    if not user_db.user_exists_in_db(username, password):
        print("Incorrect username/password, please try again.")
        return show_login_page()
         
    print("\nYou have successfully logged in.")
    active_user = user_db.get_user_by_username(username)
    
    page_history.add_page(pages.START_PAGE)
    return show_home_page(active_user)

def show_press_page(active_user):
    print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
    print("\n0 - Previous Page")

    user_input = input("\nEnter a selection: ")

    if user_input == "0":
        return show_general_useful_links_page(active_user)

    else:
        print("Invalid selection")
        return show_press_page(active_user)    

def show_search_for_user_page():
    menu.print_search_for_user_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_start_menu_page()

    else:
        print("Invalid selection. Please try again.")
        return show_search_for_user_page()

    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    if user_db.name_found_in_db(first_name, last_name):
        print("\nThey are a part of the InCollege system.")
        return show_ask_to_join_page()

    else:
        print("\nThey are not yet a part of the InCollege system.")
        return show_search_for_user_page()

def show_start_menu_page():

    print(story.STUDENT_SUCCESS_STORY)

    menu.print_start_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_login_page()

    elif user_input == "2":
        return show_create_new_account_page()

    elif user_input == "3":
        return show_watch_video_page()

    elif user_input == "4":
        return show_search_for_user_page()

    elif user_input == "5":
        page_history.add_page(pages.START_PAGE)        
        return show_useful_links_page(None)
 
    elif user_input == "6":
        page_history.add_page(pages.START_PAGE)        
        return show_important_links_page(None)

    elif user_input == "7":
        return show_exit_page()

    else:
        print("Invalid selection. Please try again.")
        return show_start_menu_page()

def show_useful_links_page(active_user):
    menu.print_useful_links_menu()

    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        return show_general_useful_links_page(active_user)

    elif user_input == "2":
        return show_browse_incollege_page(active_user)

    elif user_input == "3":
        return show_business_solutions_page(active_user)

    elif user_input == "4":
        return show_directories_page(active_user)

    elif user_input == "0" and page_history.previous_page_is_start_page():
        page_history.remove_current_page()
        return show_start_menu_page()

    elif user_input == "0" and page_history.previous_page_is_home_page():
        page_history.remove_current_page()
        return show_home_page(active_user)

    else:
        print("Invalid selection. Please try again.")
        return show_useful_links_page(active_user)

def show_watch_video_page():
    menu.print_video_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        return show_start_menu_page()

    else:
        print("\nInvalid selection.")
        return show_watch_video_page()

    print("Video is now playing.")
    return show_watch_video_page()
