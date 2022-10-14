import src.constants.pages as pages

page_history = [pages.START_PAGE]

def go_next_page(page):
    page_history.append(page)

def go_previous_page():
    if (len(page_history) > 1):
        page_history.pop()

def previous_page_is_home_page():
    return page_history[-2] == pages.HOME_PAGE

def previous_page_is_start_page():
    return page_history[-2] == pages.START_PAGE



