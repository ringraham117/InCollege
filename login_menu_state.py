def goto_start_menu_state():
  
  while True:
    menu.print_login_menu()
    user_input = input("\nEnter a selection: ")
  
    if menu.user_chose_to_login(user_input):
      goto_logging_in_state()
  
    elif menu.user_chose_to_create_new_account(user_input):
      goto_create_new_account_state()
  
    else:
      print("Invalid selection. Please try again.")
