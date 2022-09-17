from logged_in_state import goto_logged_in_state
import menu

def goto_learn_a_skill_state():
  menu.print_skills_menu()
  user_input = input("Enter a selection: ")

  if menu.user_chose_to_learn_web_dev(user_input):
    print("Under construction.")

  elif menu.user_chose_to_learn_coding():
    print("Under construction.")

  elif menu.user_chose_to_learn_communication():
    print("Under construction.")

  elif menu.user_chose_to_learn_resume_critique():
    print("Under construction.")

  elif menu.user_chose_to_learn_excel():
    print("Under construction.")

  elif menu.user_chose_to_go_to_top_level_menu():
    goto_logged_in_state()
