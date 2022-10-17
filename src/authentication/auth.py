import src.services.user_controller as userController
import src.constants.error_messages as errorMessages
import src.constants.success_messages as successMessages
import src.shared.notification_handler as notificationHandler

logged_in_user = None


def authenticate_user(user):
    userFound = userController.get_user_by_username(user.username)
    if userFound:
        if (userFound["password"] == user.password):
            global logged_in_user
            logged_in_user = userFound
            notificationHandler.display_notification(
                successMessages.SUCCESSFUL_LOGIN_MESSAGE)
            return True
        else:
            notificationHandler.display_notification(
                errorMessages.INVALID_PASSWORD_MESSAGE)
    else:
        notificationHandler.display_notification(
            errorMessages.USER_NOT_FOUND_MESSAGE)
    return False
