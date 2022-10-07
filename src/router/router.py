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
import src.pages.sign_up_page as signUpPage
import src.pages.play_video_page as playVideoPage
import src.pages.search_for_users_page as searchForUsersPage
import src.pages.ask_to_join_page as askToJoinPage
import src.pages.important_links_page as importantLinksPage
import src.pages.exit_page as exitPage

import src.pages.top_level_menu_page as topLevelMenuPage
import src.pages.job_search_page as jobSearchPage
import src.pages.find_someone_you_know_page as findSomeoneYouKnowPage
import src.pages.learn_skills_page as learnSkillsPage

# Maps page names to display_page functions
routes = {
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
  pages.LOGIN_PAGE : loginPage.display_page,
  pages.SIGN_UP_PAGE : signUpPage.display_page,
  pages.PLAY_VIDEO_PAGE : playVideoPage.display_page,
  pages.SEARCH_FOR_USERS_PAGE : searchForUsersPage.display_page,
  pages.USEFUL_LINKS_PAGE : usefulLinksPage.display_page,
  pages.IMPORTANT_LINKS_PAGE : importantLinksPage.display_page,
  pages.EXIT_PAGE : exitPage.display_page,

  pages.TOP_LEVEL_MENU_PAGE : topLevelMenuPage.display_page,
  pages.JOB_SEARCH_PAGE : jobSearchPage.display_page,
  pages.FIND_SOMEONE_YOU_KNOW_PAGE : findSomeoneYouKnowPage.display_page,
  pages.LEARN_SKILLS_PAGE : learnSkillsPage.display_page,
}

# Initialize the page history so the app starts on the "Start Page"
# page_history is a list of function names
page_history = [routes[pages.START_PAGE]]

def start_routing():
  refresh_display()

def initialize_display():
  navigate_next_page()

# Executes the last function in the page_history list
def refresh_display():
  page_history[-1]()

# page = Name of a page    
def navigate_next_page(page):
  if(page == "Exit"):
    return
  
  elif(page == "Previous Page"):
    navigate_previous_page()
  
  else:
    page_history.append(routes[page]);
  
  refresh_display()

def navigate_previous_page():
  if(len(page_history) > 1):
    page_history.pop()
   