import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
    copyright_notice = ''
    user_selection = displayOptions.display([], copyright_notice)
    router.navigate_next_page(user_selection)
