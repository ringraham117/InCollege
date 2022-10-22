import src.constants.screen_names as screenNames


def display_controller(screen_options,
                       screen_description="",
                       previousScreen=True):
  display_screen(screen_description)
  user_selection = display_screen_options(screen_options, previousScreen)
  clear_display()
  return user_selection


def display_screen_options(screen_options, previousScreen):
  formated_screen_options = format_page_options(screen_options)

  if previousScreen:
    formated_screen_options = add_previous_screen_option(
      formated_screen_options)

  for option in formated_screen_options:
    print(option, "-", formated_screen_options[option])

  user_selection = input("\nPlease select from the provided options: ")
  
  # Returns the value of the key/value pair in the formatted screen options dictionary (a string)
  return formated_screen_options.get(user_selection)


def add_previous_screen_option(screen_options):
  screen_options['0'] = screenNames.PREVIOUS_SCREEN
  return screen_options


def format_page_options(screen_options):
  formated_screen_options = {}

  option_num = 1

  for option in screen_options:
    formated_screen_options[str(option_num)] = option
    option_num += 1

  return formated_screen_options


def clear_display():
  print("\033[H\033[J", end="")


def display_screen(screen_description):
  print("\n" + "\033[94m" + screen_description + "\033[0m" + "\n")
