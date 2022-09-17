import menu

def goto_logged_in_state():
  
  menu.print_top_level_menu()
  user_input = input("\nEnter a selection: ")

  if menu.user_chose_to_find_job(user_input):
    print("Under construction.")
    goto_logged_in_state()

  elif menu.user_chose_to_find_someone(user_input):
    print("Under construction.")
    goto_logged_in_state()

  elif menu.user_chose_to_learn_a_skill(user_input):
    pass