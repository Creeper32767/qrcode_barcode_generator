import barcode
from barcode.writer import ImageWriter
from os.path import abspath
from typing import Any

barcode_types = ['code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'pzn', 'upc', 'upca']


def generate_barcode(data: Any, barcode_type: str) -> str:
    """
    a function which is used to generate barcode using the PNG format

    Args:
        data (_type_): the data that is used to generate barcode
        barcode_type (str): the type of barcode that you want to generate

    Returns:
        str: reminding message
    """    
    # Generate barcode
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_image = barcode_class(data, writer=ImageWriter())

    # Save the barcode image
    barcode_image.save(abspath("./barcode"))

    return "Barcode has been saved to 'barcode.png', which is in the current folder."

