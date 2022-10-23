import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.models.user_model as userModel

screen_options = [
    screenNames.USER_PROFILE_SCREEN,
    screenNames.SHOW_MY_NETWORK_SCREEN,
    screenNames.JOB_SEARCH_SCREEN,
    screenNames.LEARN_NEW_SKILL_SCREEN,
    screenNames.INCOLLEGE_IMPORTANT_LINKS_SCREEN,
    screenNames.USEFUL_LINKS_SCREEN,
    "Sign Out"
]


def screen():
    screen_display = "Welcome to Incollege " + auth.logged_in_user[
        "username"] + "!" "\n"

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display,
                                                       previousScreen=False)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Sign Out":
        router.screen_history = []
        auth.logged_in_user = None
        notificationHandler.display_notification(
            errorMessages.SIGN_OUT_SUCCESS_MESSAGE)
        router.navigate_user(screenNames.STARTUP_SCREEN)
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
        screen()


def handle_friend_requests():
    friend_requests = auth.logged_in_user["friend_requests"]
    if len(friend_requests) >= 1:
        notificationHandler.display_notification(
            "You have pending friend request!")
        while len(friend_requests) >= 1:
            user_id = auth.logged_in_user["user_id"]
            request_id = friend_requests[-1]
            user = userController.get_user_by_id(request_id)
            user_selection = input(user['first_name'] +
                                   " Wants to be your friend! Accept request y/n: ")
            if user_selection == 'y':
                # Add both the send and reciever to each others friend list
                userController.add_user_to_friends(user_id, request_id)
                userController.add_user_to_friends(request_id, user_id)
                userController.delete_user_friend_request(user_id, request_id)
                friend_requests.pop()
            elif user_selection == 'n':
                userController.delete_user_friend_request(user_id, request_id)
                friend_requests.pop()
            else:
                notificationHandler.display_notification(
                    errorMessages.INVALID_SELECTION_MESSAGE)


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
