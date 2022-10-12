import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  user_agreement = 'By using InCollege you agree to abide by the terms and conditions listed below. If you violate these rules, then we reserve the right to suspend your account. \nPlatform Rules:\n- The use of our platform should be related to professional networking. This is not a general forum\n- No NSFW content\n  - Discrimination based on ethnicity, religion, or political opinions will not be tolerated'

  user_selection = displayOptions.display([], user_agreement)
  router.navigate_next_page(user_selection)