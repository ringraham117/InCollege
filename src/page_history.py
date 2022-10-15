import src.constants.pages as pages

page_history = []

def add_page(page):
    page_history.append(page)

def remove_current_page():
    page_history.pop()

def previous_page_is_home_page():
    if page_history[-1] == pages.HOME_PAGE:
        return True
    
    else:
        return False

def previous_page_is_start_page():
    if page_history[-1] == pages.START_PAGE:
        return True

    else:
        return False



