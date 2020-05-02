import subprocess
import ctypes
from os import system, getuid, path
from time import sleep
import requests
from platform import system as systemos, architecture
from subprocess import check_output
from Defs.Languages import *

RED, GREEN, DEFAULT = '\033[91m', '\033[1;32m', '\033[0m'

installGetText()
languageSelector()



def checkConnection(host='https://google.com'):  # Connection check
    system('clear')
    try:
        req = requests.get(host, timeout=10)
        if req.status_code == 200:
            print("\n{1}[{0}>{1}] {0}INTERNET {0}- {2}[CONNECTED]".format(GREEN, RED,DEFAULT))
            return True
    except:
        print("\n{1}[{0}>{1}] {0}INTERNET {0}- {1}[NOT-CONNECTED]".format(GREEN, RED))
        return False


if checkConnection() == False:
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}

          {0}[{1}!{0}]{1} ^Network error^. Verify your Internet connection.\n
'''.format(RED, DEFAULT))
    exit()

def verCheck(): #Version Check For Latest Updates.
    print("\n{1}[{0}>{1}] {0}Checking For Updates{2}...".format(GREEN, RED, DEFAULT ))
    ver_url = 'https://gitlab.com/An0nUD4Y/hiddeneye/-/raw/master/version.txt'
    ver_rqst = requests.get(ver_url)
    ver_sc = ver_rqst.status_code
    if ver_sc == 200:
        with open('version.txt') as f:
            ver_current = f.read()
            ver_current = ver_current.strip()
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()
        if ver_current == github_ver:
            print("{1}[{0}+{1}] {0}[Up-To-Date]- {2}v {3}".format(GREEN, RED, DEFAULT, github_ver))
            sleep(3)
        else:
            print("{1}[{0}>{1}] {0}Their Is A Newer Version Available{2}.\n".format(GREEN, RED, DEFAULT))
            print("{1}[{0}+{1}] {0}[Current]- {2}v {3}\n{1}[{0}+{1}] {0}[Available]- {2}v.{4}".format(GREEN, RED, DEFAULT, ver_current, github_ver)) 
            print("{1}[{0}>{1}] {1}Updating To The Latest Version {0}[v {3}]... \n{1}[{0}>{1}] {0}Please Wait\n".format(GREEN, RED, DEFAULT, github_ver))
            system("git clean -d -f > /dev/null && git pull -f > /dev/null")
            with open('version.txt') as f:
                ver_current = f.read()
                ver_current = ver_current.strip()
            print("{1}[{0}>{1}] {0}Version Status After Update.{2}.\n".format(GREEN, RED, DEFAULT))
            print("{1}[{0}+{1}] {0}[Current]- {2}v {3}\n{1}[{0}+{1}] {0}[Available]- {2}v.{4}".format(GREEN, RED, DEFAULT, ver_current, github_ver))
            sleep(5)
            system("clear")
    else:
        print('{1}[{0}^{1}] {0}Failed To Get Update [Status:{1}ErrorCodeReturn{0}]\n'.format(GREEN, RED, DEFAULT))

def checkPHP(): # PHP installation Check
    if 256 != system('which php > /dev/null'): 
        print("\n{1}[{0}>{1}] {0}PHP {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
    
    else:
        print("{1}[{0}>{1}] {0}PHP {0}- {1}[NOT-INSTALLED]\n{1}[{0}>{1}] {0}Installing PHP... ".format(GREEN, RED, DEFAULT))
        system('apt-get install php > /dev/null 2>&1')
        checkPHP()
def checkNgrok():  # Ngrok check
    if path.isfile('Server/ngrok') == False:  # Is Ngrok downloaded?
        print("{1}[{0}>{1}] {0}NGROK {0}- {1}[NOT-INSTALLED]".format(GREEN, RED))
        print("{1}[{0}>{1}] {0}Installing NGROK...".format(GREEN, RED))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        req = requests.get(url , verify=False)
        with open(filename, "wb") as file_obj:
            file_obj.write(req.content)
        system('unzip ' + filename + '> /dev/null 2>&1')
        system('mv ngrok Server/ngrok > /dev/null 2>&1')
        system('rm ' + filename + '> /dev/null 2>&1')
        print("{1}[{0}>{1}] {0}NGROK {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
    elif path.isfile('Server/ngrok') == True:
        print("{1}[{0}>{1}] {0}NGROK {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))


def checkOpenport(): # Openport Check
	if 256 == system('which openport > /dev/null'):
		print("{1}[{0}>{1}] {0}OPENPORT {0}- {1}[NOT-INSTALLED]".format(GREEN, RED))
		print("{1}[{0}>{1}] {0}Installing OPENPORT...".format(GREEN, RED))
		if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
			filename = 'arm/latest.deb'
		else:
			ostype = systemos().lower()
			if architecture()[0] == '64bit':
				filename = 'debian64/latest.deb'.format(ostype)
			else:
				filename = 'debian32/latest.deb'.format(ostype)
		url = 'https://openport.io/download/' + filename
		req = requests.get(url , verify=False)
		filename2 = 'openport.deb'
		with open(filename2, "wb") as file_obj:
			file_obj.write(req.content)
		system('chmod 777 openport* > /dev/null 2>&1 && dpkg -i openport* > /dev/null 2>&1 && rm openport.deb > /dev/null 2>&1')
		checkOpenportinstall()

def checkOpenportinstall(): # Check If installed properly
    if 256 == system('which openport > /dev/null'):
        print("{1}[{0}>{1}] {0}Openport Not Installed Properly, Try installing Manually.\n{1}[{0}>{1}] {0}Check Here::( https://openport.io/download)".format(GREEN, RED))
        sleep(6)
    else:
        print("{1}[{0}>{1}] {0}OPENPORT {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
        sleep(1)

def checkPagekite(): # Check Pagekite
	if path.isfile('Server/pagekite.py') == False:
		print("{1}[{0}>{1}] {0}PAGEKITE {0}- {1}[NOT-INSTALLED]".format(GREEN, RED))
		print("{1}[{0}>{1}] {0}Installing PAGEKITE...".format(GREEN, RED))
		url = 'https://pagekite.net/pk/pagekite.py'
		req = requests.get(url , verify=False)
		filename = 'pagekite.py'
		with open(filename, "wb") as file_obj:
			file_obj.write(req.content)
		system('chmod 777 pagekite.py && mv pagekite.py Server/pagekite.py && cd Server && chmod 777 * -R')
		print("{1}[{0}>{1}] {0}PAGEKITE {0}- {2}[INSTALLED]   ({1}Pagekite only works with python2{0})".format(GREEN, RED, DEFAULT))

def checkLocalxpose():  # Localxpose check
    if path.isfile('Server/loclx') == False:  # Is Localxpose downloaded?
        print("{1}[{0}>{1}] {0}LOCALXPOSE {0}- {1}[NOT-INSTALLED]".format(GREEN, RED))
        print("{1}[{0}>{1}] {0}Installing LOCALXPOSE...".format(GREEN, RED))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        req = requests.get(url , verify=False)
        with open("loclx-linux-download.zip", "wb") as file_obj:
            file_obj.write(req.content)
        system('unzip loclx-linux-download.zip > /dev/null 2>&1 && rm loclx-linux-download.zip > /dev/null 2>&1')
        system('mv loclx-linux-* loclx > /dev/null 2>&1 && mv loclx Server/ > /dev/null 2>&1')
        print("{1}[{0}>{1}] {0}LOCALXPOSE {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
    elif path.isfile('Server/loclx') == True:
        print("{1}[{0}>{1}] {0}LOCALXPOSE {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))   

def checkLT():  # Ask to install npm,node.js,localtunnel(packages).
    if 256 == system('which lt > /dev/null'):
        print("{1}[{0}>{1}] {0}LOCALTUNNEL {0}- {1}[NOT-INSTALLED]".format(GREEN, RED))
        choice = input("\n{0}[{1}?{0}] {1}Do You Want To install LocalTunnel({0}Y{1}/{0}N{1}): {2}".format(RED, GREEN, DEFAULT)).upper()
        if choice == 'Y':
            print('')
            installLT()
        elif choice == 'N':
            print("{1}[{0}>{1}] {0}LOCALTUNNEL {0}- {1}[ABORTED]".format(GREEN, RED))
            sleep(4)
        else:
            return checkLT()
    else:
        print("{1}[{0}>{1}] {0}LOCALTUNNEL {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
        sleep(2)


def installLT():  # Localtunnel check
    print("{1}[{0}>{1}] {0}Installing LOCALTUNNEL ... {1}(Takes About 10 min.)".format(GREEN, RED))
    if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
        system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel-termux;clear")
        checkagainLT()
    else:
        system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel;clear")
        checkagainLT()


def checkagainLT():  # Check if Localtunnel installed correctly or not.
    if 256 == system('which lt > /dev/null'):
        print("{1}[{0}>{1}] {0}LOCALTUNNEL {0}- {1}[FAILED]".format(GREEN, RED))
        input("{1}[{0}>{1}] {0}Trying Again To Install Localtunnel (Press Enter)".format(GREEN, RED))
        checkLT()
    else:
        print("{1}[{0}>{1}] {0}LOCALTUNNEL {0}- {2}[INSTALLED]".format(GREEN, RED, DEFAULT))
        sleep(2)


def checkPermissions():

    if systemos() != "Windows":
        if getuid() == 0:
            print("{0}Permissions granted!".format(GREEN))
        else:
            print(
                "{0}Permissions denied! Please run as '{1}sudo{0}'".format(RED, GREEN))
            exit()
    else:
        print("{0}Windows system not yet compatible. Make sure you're using a *Unix OS.{1}".format(RED, DEFAULT))
        exit()
