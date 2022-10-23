import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.constants.error_messages as errorMessages
import src.routing.router as router
import src.services.user_controller as userController
import src.shared.console_writer as consoleWriter
import src.shared.format_input_first_upper as formatToFirstUpper
import src.shared.notification_handler as notificationHandler
import src.shared.screen_display_handler as displayHandler


def screen():
  screen_options = []

  screen_display = "Create/View Your Profile"
  user = auth.logged_in_user

  # In which case is "create profile" not in the screen options?
  if "Create Profile" not in screen_options:
    if user['has_profile'] == False:
      screen_options.append("Create User Profile")
    else:
      screen_display = "This is the profile of " + user[
        'first_name'] + " " + user['last_name'] + "!\n" + get_profile_display(
          user['title'], user['university'], user['major'],
          user['about'], user['school'], user['degree'], user['years'])
      for option in get_edit_profile_options():
        screen_options.append(option)

  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  username = auth.logged_in_user['username']

  if (screen_exists(user_selection)):
    navigate_user(user_selection)

  elif user_selection == "Create User Profile":
    title, about, experience, school, degree, years = get_user_profile_data()
    set_user_profile_data(username, title, about, experience, school, degree,
                          years, True)

  elif user_selection == "Edit Title":
    title = input("\nEnter title: ")
    userController.set_user_title(username, title)

  elif user_selection == "Edit Major":
    major = input("\nEdit Major: ")
    major = formatToFirstUpper.format_input_first_upper(major)
    userController.set_user_major(username, major)

  elif user_selection == "Edit About":
    about = input("\nEdit About: ")
    userController.set_user_about(username, about)

  elif user_selection == "Edit Experience":

    # Go to to the "edit experience" screen
    navigate_user(screenNames.EDIT_EXPERIENCE_SCREEN)

  elif user_selection == "Edit Education":
    navigate_user(screenNames.EDIT_EDUCATION_SCREEN)

    print("\nEdit Education: ")
    school = input("\n\t\tEnter school: ")
    degree = input("\n\t\tEnter degree: ")
    years = input("\n\t\tEnter years: ")
    userController.set_user_education(username, school, degree, years)

  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)

  # What does this function do?
  auth.update_logged_in_user()
  screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens


def get_user_education():
  print("\nEnter your education")
  school = input("\n\t\tEnter school: ")
  degree = input("\n\t\tEnter degree: ")
  years = input("\n\t\tEnter years: ")

  return school, degree, years


def read_past_job_details():
    
  job_title = input("\n\t\t\tEnter job title: ")
  job_employer = input("\n\t\t\tEnter employer: ")
  job_start_date = input("\n\t\t\tEnter start date: ")
  job_end_date = input("\n\t\t\tEnter end date: ")
  job_location = input("\n\t\t\tEnter location: ")
  job_description = input("\n\t\t\tEnter description: ")
  
  return (job_title, job_employer, job_start_date, job_end_date, job_location, job_description)
  

def get_user_profile_data():

  about = ""
  degree = ""
  job = ""
  school= ""
  title = ""
  years = ""
  
  # Prompt the user 
  title = input("\nEnter title: ")
  
  # Save and exit option
  consoleWriter.print_continue_profile_creation_menu()
  if not user_selects_to_continue_profile_creation():
    return title, about, job, school, degree, years
  
  # Prompt the user 
  about = input("\nEnter About: ")
  
  # Save and exit option
  consoleWriter.print_continue_profile_creation_menu()
  if not user_selects_to_continue_profile_creation():
    return title, about, job, school, degree, years
  
  # Prompt the user 
  print("\nEnter your job experience")

  # By default, a user has 0 past jobs
  job_count = 0

  # Job index starts at 0 to represent the first job in the experience list
  job_index = 0
  
  # Infinite loop
  while True:

    # Checks if the past job limit is reached
    if past_job_limit_reached(job_count):

      # Leave the loop
      break
        
    # Check to see if the user wants to add a past job
    if user_selected_to_enter_past_job():
  
      # Then, read past job details
      job_title, job_employer, job_start_date, job_end_date, job_location, job_description = read_past_job_details()

      # Call these functions to set past job details 
      userController.set_past_job_title(auth.logged_in_user["username"], job_index, job_title)
      userController.set_past_job_employer(auth.logged_in_user["username"], job_index, job_employer)
      userController.set_past_job_start_date(auth.logged_in_user["username"], job_index, job_start_date)
      userController.set_past_job_end_date(auth.logged_in_user["username"], job_index, job_end_date)
      userController.set_past_job_location(auth.logged_in_user["username"], job_index, job_location)
      userController.set_past_job_description(auth.logged_in_user["username"], job_index, job_description)
      
      # Increment the job count
      job_count += 1

      # Increment the job_index
      job_index += 1
      
    # If the user selected to not enter another past job
    else:

      # Leave the For Loop
      break

  # Save and exit option
  consoleWriter.print_continue_profile_creation_menu()
  if not user_selects_to_continue_profile_creation():
    return title, about, job, school, degree, years
  
  print("\nEnter your education")
  school = input("\n\t\tEnter school: ")
  degree = input("\n\t\tEnter degree: ")
  years = input("\n\t\tEnter years: ")
  
  return title, about, job, school, degree, years


def set_user_profile_data(username, title, about, experience, school, degree,
                          years, has_profile):
  userController.set_user_title(username, title)
  userController.set_user_about(username, about)
  userController.set_user_education(username, school, degree, years)
  userController.set_has_profile(username, has_profile)


def get_profile_display(title, university, major, about, school,
                        degree, years):
  return "\nTitle: " + title + "\nUniversity: " + university + "\nMajor: " + major + "\nAbout: " + about + "\nExperience: " + "TESTING" + "\nEducation: " + school + ", " + degree + ", " + years


def get_edit_profile_options():
  return [
    "Edit Title", "Edit Major", "Edit About", "Edit Experience",
    "Edit Education"
  ]

# Return True if the max number of past jobs is reached
# Return False if the max number of past jobs is not reached
def past_job_limit_reached(job_count):

  # If the max number of past jobs is reached
  if job_count >= 3:
  
    # Return True
    return True
  
  # Otherwise
  else:
    
    # Return False
    return False
    
# "Single responsibility principle": Each function should only do one thing
# Return True if the user selects to enter a past job
# Return False if the user selects to not enter a past job
def user_selected_to_enter_past_job():

  # Infinite loop
  while True:

    # Ask the user if they want to enter a past job
    add_job = input("\n\t\tAdd Job? (y/n): ") 
    
    # The user selects to enter a past job  
    if (add_job == "y"):
      
      # Returns True to end the function
      return True

    # The user selects to NOT enter a past job
    elif add_job == "n":    
      
      # Returns False to end the function
      return False

    # If the user enters anything else
    else:
      
      # Indicate the input is invalid 
      print("\nInvalid input")

def user_selects_to_continue_profile_creation():

  user_selection = input("Enter a selection: ")

  if user_selection == "1":
    return True

  if user_selection == "2":
    return False
  
  else:
    print("Invalid input!")
    return user_selects_to_continue_profile_creation()
  

