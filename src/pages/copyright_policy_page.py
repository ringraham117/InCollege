import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
    copyright_policy = 'You may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to InCollege without obtaining the prior written consent of InCollege.'

  
    user_selection = displayOptions.display(
        [], 
        copyright_policy
    )
  
    router.navigate_next_page(user_selection)
