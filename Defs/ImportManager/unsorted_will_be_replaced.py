from subprocess import call as run_command,Popen as run_background_command, check_output, CalledProcessError, DEVNULL
from distutils.dir_util import copy_tree as webpage_set
from time import sleep as wait
from os import path, system, chmod, stat, mkdir, remove, chdir
from shutil import rmtree, copyfile
from pathlib import Path as pathlib_Path
import re as regular_expression
import getpass, base64
