import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router


def display_page():
  brand_policy = 'InCollege users may only use InCollege trademarks in strict accordance with this policy. InCollege trademarks may be used on commercial merchandise and online only by persons and entities licensed by InCollege. InCollege should be consulted whenever it is not clear whether a proposed use is permissible. Any unauthorized use of the brand is prohibited.'
  user_selection = displayOptions.display([], brand_policy)
  router.navigate_next_page(user_selection)