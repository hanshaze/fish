class LocalizationModel:
    def __init__(self, domain: str = "HiddenEye", localedir: str = "locale"):
        self._domain = domain
        self._localedir = localedir

    @property
    def domain(self):
        # TODO add verbose output
        return self._domain

    @domain.setter
    def domain(self, new_domain):
        # TODO add verbose output
        self._domain = new_domain

    @property
    def localedir(self):
        # TODO add verbose output
        return self._localedir

    @localedir.setter
    def localedir(self, new_localedir):
        # TODO add verbose output
        self._localedir = new_localedir
