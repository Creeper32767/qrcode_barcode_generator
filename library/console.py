from os import system
from os.path import join, dirname
from sys import stdout
from time import sleep
from typing import Any
import colorama

colorama.init()


class NeatConsole(object):
    def __init__(self):
        self.path = "/"
        self.question = None

    def enter_path(self, new_path: str):
        self.path = join(self.path, new_path)

    def exit_path(self):
        self.path = dirname(self.path.rstrip('/'))

    def show_information(self):
        system("cls")
        self.execute_with_color(colorama.Fore.BLUE, print, "Now you're at: " + self.path + "\n" + "-"*20 + "\n")

    def ask_question(self, question: str) -> Any:
        """
        universal method to neatly print a form

        Args:
            question (str): the question you'd like to ask the user
        """
        self.show_information()
        self.question = question
        answer = self.execute_with_color(colorama.Fore.YELLOW, input, question)
        return answer

    def select_option(self,
                      li_options: list,
                      return_order: bool=False,
                      message: str="Type the order to select an option: ") -> Any:
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
        for order, item in enumerate(li_options):
            self.execute_with_color(colorama.Fore.GREEN, print, f"[{order}] {item}")

        # selecting an option
        order = self.execute_with_color(colorama.Fore.YELLOW, input, "\n" + message)
        if order.isdigit():
            res = li_options[int(order)]
            if return_order:
                return li_options.index(res)
            else:
                return res

    def raise_error(self, exception_msg: str):
            # handling errors
            self.execute_with_color(colorama.Fore.RED,
                                    print,
                                    f"\n[Error] Invalid data. Please try again.\nDetailed Information: {exception_msg}\n")
            for i in range(3, 0, -1):
                stdout.write(f"\rReturning in {i} seconds...")
                sleep(1)
                stdout.flush()
            self.show_information()

    def execute_with_color(self, color: colorama.Fore, func, *args: Any, **kwargs: Any) -> Any:
        """
        add color to something printed on the screen

        Args:
            color (colorama.Fore): styles defined in colorama
            func: function that prints information on the screen
        """
        print(color, end="")
        res = func(*args, **kwargs)
        print(colorama.Style.RESET_ALL, end="")
        return res
