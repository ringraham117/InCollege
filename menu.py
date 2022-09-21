def print_start_menu():

    print("\nWelcome to InCollege")
    print("--------------------")
    print("1. Login")
    print("2. Sign up")
    print("3. Play video (\"Why Join InCollege?\")")
    print("4. Search for InCollege users")


def print_top_level_menu():
    print("\nTop-level Menu")
    print("--------------")
    print("What do you want to do?")
    print("1. Search for an internship/job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Log out")


# Prints skills for the user to select
def print_skills_menu():
    print("\nLearn a Skill Menu")
    print("------------------")
    print("What skill do you want to learn?")
    print("1. Web Development")
    print("2. Coding")
    print("3. Communication")
    print("4. Resume Critique")
    print("5. Microsoft Excel")
    print("6. Return to Previous Screen")

def print_video_menu():
    print("\nPlay the \"Why Join InCollege?\" video")
    print("----------------------------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to Start Menu")

def print_search_for_user_menu():
    print("\nSearch for an active InCollege user")
    print("-------------------------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to Start Menu")

def print_find_someone_you_know_menu():
    print("\nFind someone you know")
    print("-----------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to Top-level Menu")

def print_learn_web_dev_menu():
    print("\nLearn Web Development")
    print("---------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to the Learn a Skill Menu")

def print_learn_coding_menu():
    print("\nLearn Coding")
    print("------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to the Learn a Skill Menu")    

def print_learn_communication_menu():
    print("\nLearn Communication")
    print("-------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to the Learn a Skill Menu")    

def print_learn_resume_critique_menu():
    print("\nLearn Resume Critique")
    print("---------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to the Learn a Skill Menu")    

def print_learn_excel_menu():
    print("\nLearn Microsoft Excel")
    print("---------------------")
    print("What do you want to do?")
    print("1. Continue")
    print("2. Return to the Learn a Skill Menu")    

def user_chose_to_login(user_input):
    return user_input == "1"
        
def user_chose_to_create_new_account(user_input):
    return user_input == "2"

def user_chose_to_watch_video(user_input):
    return user_input == "3"

def user_chose_to_find_job(user_input):
    return user_input == "1"        

def user_chose_to_find_someone(user_input):
    return user_input == "2"
        
def user_chose_to_learn_a_skill(user_input):
    return user_input == "3"
        
def user_chose_to_learn_web_dev(user_input):
    return user_input == "1"

def user_chose_to_learn_coding(user_input):
    return user_input == "2"
    
def user_chose_to_learn_communication(user_input):
    return user_input == "3"

def user_chose_to_learn_resume_critique(user_input):
  return user_input == "4"
    
def user_chose_to_learn_excel(user_input):
  return user_input == "5"
    
def user_chose_to_goto_top_level_menu(user_input):
  return user_input == "6"
