import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController

screen_options = ["Show Current Friends", "Unfriend"]


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
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def display_current_friends():
    user_id = auth.logged_in_user['unique_id']
    friend_ids = userController.get_user_friends(user_id)
    if (len(friend_ids) == 0):
        notificationHandler.display_notification("You have no friends!")
    else:
        for friend_id in friend_ids:
            user = userController.get_user_by_id(friend_id)
            print("Username: " + user['username'],
                  "FirstName: " + user['first_name'],
                  "LastName: " + user['last_name'],
                  "University: " + user['university'],
                  "Major: " + user['major'],
                  sep=" ")

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
                notificationHandler.display_notification(
                    "You have unfriended: " + friend_username)
            else:
                notificationHandler.display_notification(
                    "You are not friends with this user!")


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
