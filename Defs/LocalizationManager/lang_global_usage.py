#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette

hidden_eye_logo = """
 {1} ██   ██ ██ ██████   ██████   ███████ ███   ██  {2}███████ ██    ██ ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {2}██       ██  ██  ██      {0}
 {1} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {2}███████   ████   ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {2}██         ██    ██      {0}
 {1} ██   ██ ██ ██████   ██████   ███████ ██   ███  {2}███████    ██    ███████ {0}""".format(
    default_palette[4], default_palette[2], default_palette[0])

input_line = "\n{0}HiddenEye >>>  {1}".format(default_palette[0],
                                              default_palette[2])
official_website_link = "{0}https://dark-sec-official.com".format(
    default_palette[0])
by_darksec = "{0}** BY:DARKSEC **".format(default_palette[0])
line_of_dots = "{0}...............................".format(default_palette[0])
small_logo = """{1}
         _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
         |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
         |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
         {1}http://github.com/darksecdevelopers
         {0}** BY: {1}DARKSEC {0}**""".format(default_palette[0],
                                              default_palette[2])
invalid_option = "Please choose a valid option."
