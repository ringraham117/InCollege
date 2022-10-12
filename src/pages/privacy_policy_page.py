import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  privacy_policy = 'InCollege will not sell your data to any 3rd parties.\nOnly the necessary data related to your account will be used when fulfilling site requests.\nThe data we store and use includes: \n- Username\n- Password Hash\n- First Name\n- Last Name\n- Language\n- Guest Controls\n  - SMS\n  - Email\n  - Targeted Ads'

  user_selection = displayOptions.display([pages.GUEST_CONTROLS_PAGE], page_description=privacy_policy)
  router.navigate_next_page(user_selection)