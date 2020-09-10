from controllers.localization_controller import LocalizationController

# noinspection PyProtectedMember
_ = LocalizationController()._


class EULAView:
    def __init__(self):
        self.EULA_messages = {
            "eula_found": _("EULA is found"),
            "eula_is_confirmed": _("You accepted EULA"),
            "eula_is_not_confirmed": _("You didn't accept EULA, please open eula.txt"),
            "eula_not_found": _("EULA isn't found\n Generated new EULA"),
            "eula_is_invalid": _("EULA is not valid"),
            "eula_start_of_file_unconfirmed": _("# Please read and accept EULA below\n eula = False"),
            "eula_start_of_file_confirmed": _("# Please read and accept EULA below\n eula = True"),
            "eula_was_just_accepted": _("You accepted EULA, you can enjoy your HiddenEye experience"),
            "eula_was_just_rejected": _("You rejected EULA, you are not allowed to use HiddenEye"),
            "eula_power_and_responsibility_message": _("Great Power Comes With Great Responsibility"),
            "eula_do_you_accept": _("Do you accept EULA?"),
            "eula_enter_to_continue": _('Enter: "I accept EULA" to continue'),
            "eula_input_prompt": _("HiddenEye EULA>> "),
            "eula_full_disclaimer": _('''
The use of the HiddenEye & its resources/phishing-pages is COMPLETE RESPONSIBILITY of the END-USER.
Developers assume NO liability and are NOT responsible for any damage caused by this program.
Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
software to test device, company or any other type of target without WRITTEN PERMISSION from them.''')
        }
