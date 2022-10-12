import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
    page_description = ""
    
    user_selection = displayOptions.display(
    [
      pages.COPYRIGHT_NOTICE_PAGE, 
      pages.ABOUT_PAGE, 
      pages.ACCESSIBILITY_PAGE,
      pages.USER_AGREEMENT_PAGE,
      pages.PRIVACY_POLICY_PAGE, 
      pages.COOKIE_POLICY_PAGE,
      pages.COPYRIGHT_POLICY_PAGE,
      pages.BRAND_POLICY_PAGE,
      pages.GUEST_CONTROLS_PAGE,
      pages.LANGUAGES_PAGE
    ],

    page_description)

    router.navigate_next_page(user_selection)
