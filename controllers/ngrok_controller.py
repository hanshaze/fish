from pyngrok import ngrok
from pyngrok import exception as pyngrok_exceptions
from pyngrok import installer as pyngrok_installer
from pyngrok import conf as pyngrok_config


class NgrokController:
    def __init__(self, config_path: str = ".config/ngrok.yml", model=ngrok, exceptions=pyngrok_exceptions, installer=pyngrok_installer, config=pyngrok_config):
        self._model = model
        self._exceptions = exceptions
        self._installer = installer
        self._config = config
        self._config_path = config_path
        self._tunnels = None
        self._ngrok_url = None

