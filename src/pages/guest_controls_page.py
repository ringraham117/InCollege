import src.shared.display_options as displayOptions
import src.constants.pages as pages
import src.router.router as router
import database 
import state

def display_page():
  controls = database.get_guest_controls(state.loggedInUser)
  
  sms = controls['sms']
  email = controls['email']
  ads = controls['targeted_ads']
  
  user_selection = displayOptions.display([
    'SMS - On' if sms else 'SMS - Off', 
    'Email - On' if email else 'Email - Off', 
    'Targeted Ads - On' if ads else 'Targeted Ads - Off'
  ])
  
  while (user_selection != 'Previous Page'):
    if (user_selection == 'SMS - On'):
      sms = False
    elif (user_selection == 'SMS - Off'):
      sms = True
    elif (user_selection == 'Email - On'):
      email = False
    elif (user_selection == 'Email - Off'):
      email = True
    elif (user_selection == 'Targeted Ads - On'):
      ads = False
    else: 
      ads = True

    user_selection = displayOptions.display([
      'SMS - On' if sms else 'SMS - Off', 
      'Email - On' if email else 'Email - Off', 
      'Targeted Ads - On' if ads else 'Targeted Ads - Off'
    ])
    
  controls = {
    'sms': sms,
    'email': email,
    'targeted_ads': ads,
  }
  database.write_guest_controls(state.loggedInUser, controls)
  router.navigate_next_page(user_selection)
  