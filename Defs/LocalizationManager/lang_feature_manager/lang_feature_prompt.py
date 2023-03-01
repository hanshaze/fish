#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

feature_prompt = {
    "feature_alert": _("---------------------------------------------------------\n{0}[ PROMPT: PLEASE CHOOSE FEATURES YOU WOULD LIKE TO USE. ]{1} {0}\n---------------------------------------------------------".format(default_palette[0], default_palette[4])),
    "keylogger": _("\n{0}[{1}A{0}]{1} KEYLOGGER (Usually Kills Connection) ".format(default_palette[0], default_palette[2])),
    "cloudfare":_("\n{0}[{1}B{0}]{1} FAKE CLOUDFARE PROTECTION PAGE ".format(default_palette[0], default_palette[2])),
    "email":_("\n{0}[{1}C{0}]{1} CAPTURED DATA EMAILED ".format(default_palette[0], default_palette[2])),
    "none":_("\n{0}[{1}0{0}]{1} PRESS ONLY ENTER FOR NONE OF THE ABOVE ".format(default_palette[0], default_palette[2])),
    "example":_("\n{0}[{1}*{0}]{1} Please type all together. Eg: ABC or AC {0}[{1}*{0}]{1}".format(default_palette[0], default_palette[2])),
}
