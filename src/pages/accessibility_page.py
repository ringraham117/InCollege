import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
    accessibility = 'You may use this app for purposes of meeting others who are in college. Through the app, you may perform functions such as connecting with other users, finding a job, learning skills, etc. From time to time this app may be updated to provide other features and functionality. Any unauthorized use of this app is prohibited'
    user_selection = displayOptions.display([], page_description=accessibility)
    router.navigate_next_page(user_selection)
