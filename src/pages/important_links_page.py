<<<<<<< HEAD
import src.shared.display_options as displayOptions
import src.constants.pages as pages
=======
import src.constants.pages as pages
import src.shared.display_options as displayOptions
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
import src.router.router as router


def display_page():
<<<<<<< HEAD
    user_selection = displayOptions.display([
        pages.COPYRIGHT_NOTICE_PAGE, pages.COOKIE_POLICY_PAGE,
        pages.PRIVACY_POLICY_PAGE, pages.ACCESSIBILITY_PAGE,
        pages.USER_AGREEMENT_PAGE, pages.BRAND_POLICY_PAGE
    ])
    router.navigate_next_page(user_selection)
=======
  page_description = "Important InCollege Links - INCOMPLETE"
  user_selection = displayOptions.display(
    [
      pages.LOGIN_PAGE,
      pages.SIGN_UP_PAGE,
      pages.START_PAGE
    ],
     
    page_description)
  
  router.navigate_next_page(user_selection)
>>>>>>> 780721faf639475c43e1bfa8c5d8ebd416e34be8
