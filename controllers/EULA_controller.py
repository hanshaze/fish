import pathlib
import stat
from os import chmod
from time import sleep

from views.EULA_view import EULAView


class EULAController:
    def __init__(self, confirmation_text: str = "eula = True"):
        self.eula = "eula.txt"
        self.confirmation_text = confirmation_text
        self.license = open("LICENSE", "r")

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
        with open(str(self.eula), "w+") as temp_eula:
            chmod(self.eula, 0o777)
            temp_eula.write("{0}\n{1}".format(
                EULAView().EULA_messages["eula_start_of_file_unconfirmed"],
                text_license,
            ))
            temp_eula.close()

    def check_eula_confirmation(self):
        with open(self.eula, "r") as file:
            if self.confirmation_text in file.read():
                print(EULAView().EULA_messages["eula_is_confirmed"])
                return True
            else:
                print(EULAView().EULA_messages["eula_is_not_confirmed"])
                return False

    def confirm_eula(self):
        # FIXME replace those strings with View entries
        print(
            f"{self.license.read()}\nGreat Power Comes With Great Responsibility\n"
        )
        print(
            "The use of the HiddenEye & its resources/phishing-pages is COMPLETE RESPONSIBILITY of the END-USER."
        )
        print(
            "Developers assume NO liability and are NOT responsible for any damage caused by this program."
        )
        print(
            "Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this"
        )
        print(
            "software to test device, company or any other type of target without WRITTEN PERMISSION from them."
        )
        print('Do you accept EULA? \n\nEnter: "I accept EULA" to continue\n')
        answer = input("HiddenEye EULA>> ").lower().replace(" ", "")
        if answer == "iaccepteula":
            eula_temp_input = open(self.eula, "rt")
            eula_temp_data = eula_temp_input.read().replace(
                EULAView().EULA_messages["eula_start_of_file_unconfirmed"],
                EULAView().EULA_messages["eula_start_of_file_confirmed"],
            )
            eula_temp_input.close()
            eula_temp_input = open(self.eula, "wt")
            eula_temp_input.write(eula_temp_data)
            eula_temp_input.close()
            print(EULAView().EULA_messages["eula_was_just_accepted"])
            sleep(3.5)
            pass
        else:
            print(EULAView().EULA_messages["eula_was_just_rejected"])
            sleep(3.5)
            exit()
