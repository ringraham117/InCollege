import src.pages.general_page as generalPage
import src.pages.about_page as aboutPage
import src.pages.blog_page as blogPage
import src.pages.help_center_page as helpCenterPage
import src.pages.press_page as pressPage
import src.pages.careers_page as careersPage
import src.pages.developers_page as developersPage

import src.pages.useful_links_page as usefulLinksPage
import src.pages.browse_incollege_page as browseInCollegePage
import src.pages.business_solutions_page as businessSolutionsPage
import src.pages.directories_page as directoriesPage

import src.constants.pages as pages

import src.pages.start_page as startPage
import src.pages.login_page as loginPage

routes = {
  pages.USEFUL_LINKS_PAGE : usefulLinksPage.display_page,
  pages.BROWSE_INCOLLEGE_PAGE : browseInCollegePage.display_page,
  pages.BUSINESS_SOLUTIONS_PAGE : businessSolutionsPage.display_page,
  pages.DIRECTORIES_PAGE : directoriesPage.display_page,
  pages.GENERAL_PAGE : generalPage.display_page,
  pages.PRESS_PAGE : pressPage.display_page,
  pages.HELP_CENTER_PAGE : helpCenterPage.display_page,
  pages.DEVELOPERS_PAGE : developersPage.display_page,
  pages.CAREERS_PAGE : careersPage.display_page,
  pages.BLOG_PAGE : blogPage.display_page,
  pages.ABOUT_PAGE : aboutPage.display_page,
  pages.START_PAGE : startPage.display_page,
  pages.LOGIN_PAGE : loginPage.display_page
  # This part needs refactor from the state object
}

# Initialize the page history so the app starts on the "Start Page"
page_history = [routes[pages.START_PAGE]]

def start_routing():
  refresh_display()

def initialize_display():
  navigate_next_page()

def refresh_display():
    page_history[-1]()

# page = Name of a page    
def navigate_next_page(page):
  if(page == "Previous Page"):
    navigate_previous_page()
  else:
    page_history.append(routes[page]);
  
  refresh_display()

def navigate_previous_page():
  if(len(page_history) > 1):
    page_history.pop()
   