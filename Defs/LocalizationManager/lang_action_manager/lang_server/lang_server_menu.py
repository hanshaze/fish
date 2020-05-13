#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#

import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

lang_server_selection = {
    "server_selection" : _('{0}[ HOSTING SERVER SELECTION ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "select_any_available_server" : _('\n {0}[{1}*{0}]{0}Select Any Available Server:{1}').format(default_palette[0], default_palette[4]),
    "servers_list" :
    [ ['{0}[{1}00{0}]{1}Localhost', '{0}[{1}04{0}]{1}Localtunnel (not working now)'],
      ['{0}[{1}01{0}]{1}Ngrok', '{0}[{1}05{0}]{1}OpenPort (not working now)'],
      ['{0}[{1}02{0}]{1}Serveo', '{0}[{1}06{0}]{1}Pagekite (not working now)'],
      ['{0}[{1}03{0}]{1}Localxpose (not working now)']]
}
