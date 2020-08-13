import pathlib
from os import chmod
import stat
from views.EULA_view import EULAView


class EULAController:
    def __init__(self, confirmation_text: str = 'eula = True'):
        self.eula = "eula.txt"
        self.confirmation_text = confirmation_text
        self.license = open("LICENSE", 'r')

    def check_eula_existence(self):
        """
        :return: True if self.eula exists
        """
        if pathlib.Path(self.eula).exists():
            print(EULAView().EULA_messages["eula_found"])
            return True
        print(EULAView().EULA_messages["eula_not_found"])
        return False

    def generate_new_eula(self):
        pathlib.Path(str(self.eula)).touch(exist_ok=True)
        text_license = self.license.read()
        with open(str(self.eula), 'w+') as temp_eula:
            chmod(self.eula, 0o777)
            temp_eula.write("{0}\n{1}".format(EULAView().EULA_messages["eula_start_of_file_unconfirmed"], text_license))
            temp_eula.close()

    def check_eula_confirmation(self):
        with open(self.eula, 'r') as file:
            if self.confirmation_text in file.read():
                print(EULAView().EULA_messages["eula_is_confirmed"])
                return True
            else:
                print(EULAView().EULA_messages["eula_is_not_confirmed"])
                return False
