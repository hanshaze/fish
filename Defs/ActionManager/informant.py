from Defs.ThemeManager.theme import default_palette
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.EmailManager.email_prompt import captured_data_email_request

def exit_message(port):  # Message when HiddenEye exit
    choice = input(
        "\n\n{0}[{1}?{0}] Re-run(r) : Exit(x) : Send Email(M) : SelectServer(S)\n\n >> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'R' or choice == 'r':
        run_command('sudo python3 HiddenEye.py')
    elif choice == 'M' or choice == 'm':
        captured_data_email_request(port)
    elif choice == 'S' or choice == 's':
    	returnServer(port)
    elif choice == 'X' or choice == 'x':
        run_command('clear')
        print('''
                  {1}HIDDEN EYE {1}BY: DARKSEC TEAM
            {0}https://dark-sec-official.com
  {1}  [[*]] IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.
  {0}
     [{1}!{0}] PLEASE LET US KNOW , IF ANY PHISHING PAGE GOT BROKEN .
     [{1}!{0}] MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
     [{1}!{0}] IF YOU HAVE MORE PHISHING PAGES, THEN JUST MAKE A PULL REQUEST.
     [{1}!{0}] PLEASE DON'T HARM ANYONE , ITS ONLY FOR EDUCATIONAL PURPOSE.
     [{1}!{0}] WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL

  {1}  [[*]] THANKS FOR USE THIS TOOL. HAPPY HACKING ... GOOD BYE \n '''.format(default_palette[2], default_palette[0]))
    else:
        run_command('clear')
        return exit_message(port)