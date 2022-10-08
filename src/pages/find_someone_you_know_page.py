import menu
import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router


def display_page():
    menu.print_find_someone_you_know_menu()
    user_input = input("\nEnter a selection: ")

    if user_input == "1":
        pass

    elif user_input == "2":
        router.navigate_next_page(pages.TOP_LEVEL_MENU_PAGE)

    else:
        print("Invalid selection")
        router.navigate_next_page(pages.FIND_SOMEONE_YOU_KNOW_PAGE)

    print("\nUnder Construction.")
    router.navigate_next_page(pages.FIND_SOMEONE_YOU_KNOW_PAGE)
