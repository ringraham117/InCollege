import login_module
import menu_module

menu_module.print_login_menu()

user_input = input("\nEnter a selection: ")

if user_chose_to_login():
    
    menu_module.print_login_menu()

    print("\nLogin:")
    username = input("Username: ")
    password = input("Password: ")

    

elif user_chose_to_create_new_account():
    login_module.create_new_user()
