from controllers.localization_controller import LocalizationController

# noinspection PyProtectedMember
_ = LocalizationController()._


class ConnectionView:
    def __init__(self):
        self.connection_messages = {
            # TODO add verbose messages for model
            "connection_is_detected": _("You have internet connection, proceeding..."),
            "connection_is_not_detected": _("Please verify your internet connection before launching")
        }
