def print_login_menu():

  print("\nInCollege")
  print("---------")
  print("1. Login")
  print("2. Sign up")

def print_top_level_menu():

  print("\n1. Search for an internship/job")
  print("2. Find someone you know")
  print("3. Learn a new skill")


# Prints skills for the user to select
def print_skills_menu():
  print("\n1. Web Development")
  print("2. Coding")
  print("3. Communication")
  print("4. Resume Critique")
  print("5. Microsoft Excel")
  print("6. Return to Previous Screen")

def user_chose_to_login(user_input):
  if user_input == "1":
    return True

  else:
    return False

def user_chose_to_create_new_account(user_input):
  if user_input == "2":
    return True

  else:
      return False

def user_chose_to_find_job(user_input):
  if user_input == "1":
      return True

  else:
    return False

def user_chose_to_find_someone(user_input):
  if user_input == "2":
      return True

  else:
    return False

def user_chose_to_learn_a_skill(user_input):
  if user_input == "3":
    return True

  else:
    return False