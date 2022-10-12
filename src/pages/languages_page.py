import database as db
import src.constants.pages as pages
import src.shared.display_options as displayOptions
import src.router.router as router
import state

def display_page():
    
    # Check if no one is logged in
    if state.loggedInUser == "":
        print("\nPlease login to change language settings")
        return router.navigate_next_page("Previous Page")
    
    # Present the user with options
    print("\n1 - English")
    print("2 - Spanish")
    print("3 - Return to previous screen")

    # Read the user's input
    user_input = input("\nMake a selection: ")
  
    # Handle the user's input
    if user_input == "1":
        language_selection = "English"

    elif user_input == "2":
        language_selection = "Spanish"

    elif user_input == "3":
        return router.navigate_next_page("Previous Page")
        
    else:
        print("Invalid selection.")

    print("\nLanguage was set to " + language_selection)

    # Get a reference to the list of users
    database = db.get_db_as_dictionary()

    # Iterate through each user
    for user in database["users_list"]:
        
        # If the iterator's username matches that of the logged in user
        if user["username"] == state.loggedInUser:
            
            # Sets the iterator's language setting based on the language selection
            user["language"] = language_selection

    # Update the database with the update list of users
    db.update_users_list(database)

    # Returns to the previous page (Important links page)
    router.navigate_next_page("Previous Page")
