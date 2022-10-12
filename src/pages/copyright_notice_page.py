import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
    copyright_notice = 'The InCollege name and branding are protected under Copyright'
    user_selection = displayOptions.display([], copyright_notice)
    router.navigate_next_page(user_selection)
