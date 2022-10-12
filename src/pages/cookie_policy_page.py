import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  cookies_policy = 'InCollege uses cookies to enhance the user experience in the application. This includes basic information on your current session and the pages you navigate to while logged in. Additional cookies are used for targeted advertising, bringing you ads that you would like to see. These may track your browsing on other sites. To turn off targeted advertising, navigate to InCollege Important Links -> Guest Controls then select Targeted Ads to toggle on or off, these are on by default'

  user_selection = displayOptions.display([], cookies_policy)
  router.navigate_next_page(user_selection)