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
        print(
            f'{self.license.read()}\n{EULAView().EULA_messages["eula_power_and_responsibility_message"]}\n')
        print(EULAView().EULA_messages["eula_full_disclaimer"])
        print(
            f'{EULAView().EULA_messages["eula_do_you_accept"]} \n\n{EULAView().EULA_messages["eula_enter_to_continue"]}\n')
        answer = input(
            EULAView().EULA_messages["eula_input_prompt"]).lower().replace(" ", "")
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
            sleep(1.5)
            pass
        else:
            print(EULAView().EULA_messages["eula_was_just_rejected"])
            sleep(1.5)
            exit()
