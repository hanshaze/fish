#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#



import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

lang_exit_message = {
    "choice" : _('\n{0}[{1}?{0}] Re-run(r) : Exit(x) : Send Email(m) : SelectServer(s)\n\n >> {2}').format(default_palette[0], default_palette[4], default_palette[2]),
    "help_to_improve_this_tool" : _('{1}  [[*]] {0}You always can help to improve this tool and support us. {0}').format(default_palette[2], default_palette[0]),
    "tell_if_page_got_broken" : _('{0}[{1}!{0}] If any phishing page got broken, please let us know.').format(default_palette[2], default_palette[0]),
    "make_your_pull_request_or_issue" :  _('{0}[{1}!{0}] You can create issue or pull request on our GitHub page.').format(default_palette[2], default_palette[0]),
    "small_disclaimer_suggestion" : _("{0}[{1}!{0}] We are not responsible for anything you do with this tool, please review license agreement when you have some time. \n{0}[{1}!{0}] We know everyone skips it and just agrees, but please, don't act so irresponsible with any software you use.").format(default_palette[2], default_palette[0]),
    "forum_suggestion" : _('{0}[{1}!{0}] Our website has forum, please visit it, we want to build great community for all of you, we are always happy to have your help.').format(default_palette[2], default_palette[0]),
    "financial_support" : _("{0}[{1}!{0}] If you want to support us with finances - visit our patreon page: (here_will_be_link_soon)").format(default_palette[2], default_palette[0]),
    "thank_you" : _('{0}[{1}!{0}] You help us even when you just use this tool. Everyone at {1}DarkSec{0} happy to have you, thank you very much! Have a nice day!').format(default_palette[2], default_palette[0])
}