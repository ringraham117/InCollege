def display(options, page_description = ""):
  print(page_description + "\n")
  
  page_options = format_page_options(options)

  for option in page_options:
    print(option, "-", page_options[option])

  user_selection = input("\nPlease select from the above Pages: ")

  while(True):
    if(user_selection in page_options):
      return page_options[user_selection]
    else:
      user_selection = input("\nPlease select from the above Pages: ")


def format_page_options(options):
  page_options = {}
  option_num = 1;
  for option in options:
    page_options[str(option_num)] = option
    option_num += 1
  
  page_options["0"] = "Previous Page"
  
  return page_options;