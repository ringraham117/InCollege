import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
    user_selection = displayOptions.display([
        pages.COPYRIGHT_NOTICE_PAGE, pages.COOKIE_POLICY_PAGE,
        pages.PRIVACY_POLICY_PAGE, pages.ACCESSIBILITY_PAGE,
        pages.USER_AGREEMENT_PAGE, pages.BRAND_POLICY_PAGE
    ])
    router.navigate_next_page(user_selection)
