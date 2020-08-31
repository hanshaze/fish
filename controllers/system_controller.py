from os import name


class SystemController:
    def __init__(self, sys_name=name):
        self._sys_name = sys_name

    def is_unix(self):
        return True if self._sys_name == 'posix' else False
