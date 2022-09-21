def print_start_menu():

    print("\nInCollege")
    print("---------")
    print("1. Login")
    print("2. Sign up")


def print_top_level_menu():

    print("\nWhat do you want to do?")
    print("1. Search for an internship/job")
    print("2. Find someone you know")
    print("3. Learn a new skill")


# Prints skills for the user to select
def print_skills_menu():
    print("\nWhat skill do you want to learn?")
    print("1. Web Development")
    print("2. Coding")
    print("3. Communication")
    print("4. Resume Critique")
    print("5. Microsoft Excel")
    print("6. Return to Previous Screen")

def user_chose_to_login(user_input):
  return user_input == "1"

def user_chose_to_create_new_account(user_input):
  return user_input == "2"    

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
