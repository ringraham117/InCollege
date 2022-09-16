import login_module
import menu_module

while True:
  menu_module.print_login_menu()
  
  user_input = input("\nEnter a selection: ")
  
  if user_input == "1":
      login_module.login()
  
  elif user_input == "2":
      login_module.create_new_user()
