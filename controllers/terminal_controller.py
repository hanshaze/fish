from subprocess import call
from controllers.system_controller import SystemController


class TerminalController:
    def __init__(self):
        pass

    @staticmethod
    def clear():
        call('clear' if SystemController().is_unix() else 'cls')
