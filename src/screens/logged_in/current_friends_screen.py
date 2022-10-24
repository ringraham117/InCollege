import src.authentication.auth as auth
import src.constants.error_messages as errorMessages
import src.constants.screen_names as screenNames
import src.routing.router as router
import src.screens.logged_in.create_profile_screen as createProfileScreen
import src.services.user_controller as userController
import src.shared.notification_handler as notificationHandler
import src.shared.screen_display_handler as displayHandler


screen_options = ["Show Current Friends", "Unfriend", "Show Friend Profile"]


def screen():
  screen_display = "Current Friends Screen!"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  elif user_selection == "Show Current Friends":
    display_current_friends()
  elif user_selection == "Unfriend":
    handle_unfriend()
  elif user_selection == "Show Friend Profile":
    friend_id = input("Enter Friend ID: ")
    user = userController.get_user_by_id(friend_id)
    if user == None:
      notificationHandler.display_notification("Invalid Friend ID!")
    elif friend_id not in auth.logged_in_user['friends']:
      notificationHandler.display_notification("This user is not your friend!")
    else:
      display_user_profile(user)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
  screen()


def handle_unfriend():
  user_id = auth.logged_in_user['unique_id']
  friend_ids = userController.get_user_friends(user_id)
  if (len(friend_ids) == 0):
    notificationHandler.display_notification(
      "You have no friends to unfriend!")
  else:
    friend_username = input(
      "Enter the username of the friend you want to unfriend: ")
    friend = userController.get_user_by_username(friend_username)
    if (friend == None):
      notificationHandler.display_notification(
        errorMessages.USER_NOT_FOUND_MESSAGE)
    else:
      friend_id = friend['unique_id']
      if (friend_id in friend_ids):
        friend_id = friend['unique_id']
        userController.delete_user_friend(user_id, friend_id)
        userController.delete_user_friend(friend_id, user_id)
        notificationHandler.display_notification("You have unfriended: " +
                                                 friend_username)
      else:
        notificationHandler.display_notification(
          "You are not friends with this user!")


def display_current_friends():
  user_id = auth.logged_in_user['unique_id']
  friend_ids = userController.get_user_friends(user_id)
  if (len(friend_ids) == 0):
    notificationHandler.display_notification("You have no friends!")
  else:
    for friend_id in friend_ids:
      user = userController.get_user_by_id(friend_id)
      print("\nUsername: " + user['username'],
            "\nFirstName: " + user['first_name'],
            "\nLastName: " + user['last_name'],
            "\nUniversity: " + user['university'], "\nMajor: " + user['major'])
      if user['has_profile'] == True:
        print("\033[92m" + "Profile Available! | Friend ID: " +
              user['unique_id'] + "\033[0m")


def display_user_profile(user):
  if user['has_profile'] == True:
    print("\033[92m" + "\nUser: " + "\033[0m" + user['first_name'],
          user['last_name'],
          "\033[92m" + "\nTitle: " + "\033[0m" + "\033[0m" + user['title'],
          "\033[92m" + "\nUniversity: " + "\033[0m" + user['university'],
          "\033[92m" + "\nMajor: " + "\033[0m" + user['major'],
          "\033[92m" + "\nAbout: " + "\033[0m" + user['about'],
          "\033[92m" + "\nExperience: " + "\033[0m" + createProfileScreen.get_formatted_job_experience(user, "job_1") + createProfileScreen.get_formatted_job_experience(user, "job_2") + createProfileScreen.get_formatted_job_experience(user, "job_3") +
          "\033[92m" + "\nEducation: " + "\033[0m" + user["school"] + ", " + user["degree"] + ", " + user["years"])
  else:
    notificationHandler.display_notification("User doesn't have a profile")


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
