from gettext import gettext as _


class EULAView:
    def __init__(self):
        self.EULA_messages = {
            "eula_found": _("EULA is found"),
            "eula_is_confirmed": _("You accepted EULA"),
            "eula_is_not_confirmed": _("You didn't accept EULA, please open eula.txt"),
            "eula_not_found": _("EULA isn't found\n Generated new EULA"),
            "eula_is_invalid": _("EULA is not valid"),
            "eula_start_of_file_unconfirmed": _("# Please read and accept EULA below\n eula = False"),
            "eula_start_of_file_confirmed": _("# Please read and accept EULA below\n eula = True")
        }
