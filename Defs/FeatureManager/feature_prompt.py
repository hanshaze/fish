#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
from time import sleep

import Defs.FeatureManager.cloudflare as cloudflare
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.FeatureManager.keylogger as keylogger
import Defs.LocalizationManager.lang_feature_manager.lang_feature_prompt as feature_localization
import Defs.LocalizationManager.lang_global_usage as global_localization
import Defs.ThemeManager.theme as theme
from Defs.ImportManager.unsorted_will_be_replaced import run_command

default_palette = theme.default_palette


def feature_prompt():
    run_command("clear")
    print(global_localization.small_logo)
    print(feature_localization.feature_prompt["feature_alert"])
    print(feature_localization.feature_prompt["keylogger"])
    print(feature_localization.feature_prompt["cloudfare"])
    print(feature_localization.feature_prompt["email"])
    print(feature_localization.feature_prompt["none"])
    print(feature_localization.feature_prompt["example"])
    option = input(global_localization.input_line).lower()

    letters = ["a", "b", "c"]

    for x in option:
        if x in letters:
            if "a" in x:
                keylogger.add_keylogger()
            elif "b" in x:
                cloudflare.add_cloudfare()
            elif "c" in x:
                email_prompt.captured_data_email_configuration_prompt()
        else:
            print(global_localization.invalid_option)
            sleep(3)
            feature_prompt()
