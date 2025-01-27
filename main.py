import colorama
from os import system
from os.path import join, dirname
from time import sleep
from library import generate_barcode, generate_qrcode, read_barcode_qrcode, barcode_types
from typing import Any

colorama.init()


class NeatConsole(object):
    def __init__(self):
        self.path = "/"
        self.question = None
        self.show_information()

    def enter_path(self, new_path: str):
        self.path = join(self.path, new_path)

    def exit_path(self):
        self.path = dirname(self.path.rstrip('/'))

    def show_information(self):
        system("cls")
        print(colorama.Fore.BLUE + "Now you're at: " + self.path + "\n" + "-"*20 + "\n" + colorama.Fore.RESET)

    def ask_question(self, question: str) -> Any:
        """
        universal method to neatly print a form

        Args:
            question (str): the question you'd like to ask the user
        """
        self.show_information()
        self.question = question
        answer = input(colorama.Fore.YELLOW + question + colorama.Fore.RESET)
        return answer

    def re_ask_question(self):
        if self.question is not None:
            print(colorama.Fore.RED + "[Error] Invalid data. Please try again." + colorama.Fore.RESET)
            sleep(1)
            self.show_information()
            self.ask_question(self.question)

    def select_option(self, li_options: list, return_order: bool=False, message: str="Type the order to select an option: ") -> Any:
        """
        universal method to select one element in a list.

        Args:
            li_options (list): alternative elements
            return_order (bool): if return yhe order directly. Defaults to False.
            message (str): reminding message. Defaults to "Type the order to select an option."

        Returns:
            Any: one element of the choices
        """
        self.show_information()
        print(colorama.Fore.GREEN, end="")
        for item in li_options:
            print(f"[{li_options.index(item)}] {item}")

        # selecting an option
        order = input(message)
        print("\n" + colorama.Fore.RESET, end="")
        if order.isdigit():
            try:
                res = li_options[int(order)]
                if return_order:
                    return li_options.index(res)
                else:
                    return res
            except IndexError:
                pass

            # handling errors
            print(colorama.Fore.RED + "[Error] Invalid data. Please try again." + colorama.Fore.RESET)
            sleep(1)
            self.show_information()
            self.select_option(li_options, return_order, message)


if __name__ == "__main__":
    console = NeatConsole()
    choice = console.select_option(["EXIT", "Read Barcode or QRCode", "Generate Barcode", "Generate QRCode", "Read LICENSE"])
    console.enter_path(choice)
    qrcode_description = ["ERROR_CORRECT_L  About 7% or less errors can be corrected.",
                          "ERROR_CORRECT_M  About 15% or less errors can be corrected.",
                          "ERROR_CORRECT_Q  About 25% or less errors can be corrected.",
                          "ERROR_CORRECT_H  About 30% or less errors can be corrected."]
    if choice == "EXIT":
        pass

    elif choice == "Read Barcode or QRCode":
        path = console.ask_question("[1/1] Please enter a valid path: ")
        data = read_barcode_qrcode(path)
        print("Information included in the barcode or qrcode: ", *data, sep="\n")

    elif choice == "Generate Barcode":
        types = console.select_option(barcode_types, message="[1/2] Type the order to select an option: ")
        data = console.ask_question("[2/2] Please enter some data: ")
        if data == "":
            data = console.re_ask_question()

        try:
            print(generate_barcode(data, types))
        except Exception as err:
            print(colorama.Fore.RED + str(err) + colorama.Fore.RESET)

    elif choice == "Generate QRCode":
        version = int(console.ask_question("[1/3] Please enter a version(from 1 to 40): "))
        error_correction = console.select_option(qrcode_description,
            return_order=True,
            message="[2/3] Type the order to select an option: "
        )
        data = console.ask_question("[3/3] Please enter some data: ")
        if data == "":
            data = console.re_ask_question()

        try:
            print(generate_qrcode(data, error_correction, version))
        except Exception as err:
            print(colorama.Fore.RED + str(err) + colorama.Fore.RESET)

    elif choice == "Read LICENSE":
        with open("./LICENSE", encoding="utf-8") as fp:
            print(fp.read())

    input("Finished. Press 'Enter' to exit.")
