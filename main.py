from library import generate_barcode, generate_qrcode, read_barcode_qrcode, barcode_types, NeatConsole
import colorama

qrcode_description = ["ERROR_CORRECT_L  About 7% or less errors can be corrected.",
                      "ERROR_CORRECT_M  About 15% or less errors can be corrected.",
                      "ERROR_CORRECT_Q  About 25% or less errors can be corrected.",
                      "ERROR_CORRECT_H  About 30% or less errors can be corrected."]

colorama.init()
console = NeatConsole()


def wrapper_read_barcode_qrcode():
    try:
        path = console.ask_question("[1/1] Please enter a valid path: ")
        data = read_barcode_qrcode(path)
        print("Information included in the barcode or qrcode: ", *data, sep="\n")
    except Exception as err:
        console.raise_error(str(err))
        wrapper_read_barcode_qrcode()


def wrapper_generate_barcode():
    try:
        types = console.select_option(barcode_types, message="[1/2] Type the order to select an option: ")
        data = console.ask_question("[2/2] Please enter some data: ")
        print(generate_barcode(data, types))
    except Exception as err:
        console.raise_error(str(err))
        wrapper_generate_barcode()


def wrapper_generate_qrcode():
    try:
        version = int(console.ask_question("[1/3] Please enter a version(from 1 to 40): "))
        error_correction = console.select_option(qrcode_description,
                                                 return_order=True,
                                                 message="[2/3] Type the order to select an option: ")
        data = console.ask_question("[3/3] Please enter some data: ")
        print(generate_qrcode(data, error_correction, version))
    except Exception as err:
        console.raise_error(str(err))


def main():
    choice = console.select_option(["EXIT", "Read Barcode or QRCode", "Generate Barcode", "Generate QRCode", "Read LICENSE"])
    console.enter_path(choice)

    if choice == "EXIT":
        pass

    elif choice == "Read Barcode or QRCode":
        wrapper_read_barcode_qrcode()

    elif choice == "Generate Barcode":
        wrapper_generate_barcode()

    elif choice == "Generate QRCode":
        wrapper_generate_qrcode()

    elif choice == "Read LICENSE":
        with open("./LICENSE", encoding="utf-8") as fp:
            console.execute_with_color(colorama.Fore.CYAN, print, fp.read())


if __name__ == "__main__":
    main()
    input("Finished. Press 'Enter' to exit.")
