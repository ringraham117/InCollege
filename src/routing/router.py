import src.routing.routes as routes

import src.constants.screen_names as screenNames
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notifcationHandler

screen_history = []


def navigate_user(screen_name):
    if (screen_name == screenNames.PREVIOUS_SCREEN):
        remove_display()
    else:
        screen = get_screen(screen_name)
        add_display(screen)

    refresh_display()


def add_display(screen):
    screen_history.append(screen)


def remove_display():
    if (len(screen_history) > 1):
        screen_history.pop()
    else:
        notifcationHandler.display_notification(
            errorMessages.PREVIOUS_PAGE_UNAVAILABLE)


def refresh_display():
    screen_history[-1]()


def get_screen(screen_name):
    return routes.screen_functions[screen_name]
