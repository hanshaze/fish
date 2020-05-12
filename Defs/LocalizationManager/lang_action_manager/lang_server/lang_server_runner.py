#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#

import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

lang_start_localhost = {
    "localhost_server" : _('\n{0}[ LOCALHOST SERVER ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "your_localhost_is" : _('Your Localhost is '),
    "starting_server_on_addr" : _('\n[*] Starting Server On Address:: {0}:{1}'),
    "running_localhost_server" : _('\n{0}[ RUNNING LOCALHOST SERVER ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _('\n{0}[{1}!{0}]{1} SEND THIS URL TO TARGETS ON SAME NETWORK').format(default_palette[0], default_palette[2]),
    "localhost_url" : _('\n{0}[{1}*{0}]{1} Localhost URL: {2}http://').format(default_palette[2], default_palette[3], default_palette[3])
}

lang_start_ngrok = {
    "ngrok_server" : _('\n{0}[ NGROK SERVER ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _("\n{0}[{1}!{0}]{1} SEND THIS NGROK URL TO TARGETS").format(default_palette[0], default_palette[2]),
    "ngrok_url" : _('\n{0}[{1}*{0}]{1} NGROK URL: {2}').format(default_palette[0], default_palette[2], default_palette[3])
}

lang_start_serveo = {
    "serveo_random_server" : _('\n{0}[ RANDOM SERVEO URL ]{1}!! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _('\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO TARGETS').format(default_palette[0], default_palette[4]),
    "serveo_url" : _('\n{0}[{1}*{0}]{1} SERVEO URL: {2}').format(default_palette[0], default_palette[4], default_palette[3])

}