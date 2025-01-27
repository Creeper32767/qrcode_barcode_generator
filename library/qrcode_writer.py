import qrcode
from os.path import abspath
from typing import Any

li_error_correction = [qrcode.constants.ERROR_CORRECT_L,
                       qrcode.constants.ERROR_CORRECT_M,
                       qrcode.constants.ERROR_CORRECT_Q,
                       qrcode.constants.ERROR_CORRECT_H]


def generate_qrcode(data: Any, error_correction_order: int=0, version: int=1) -> str:
    """
    a function which is used to generate qrcode.

    Args:
        data (Any): the data that is used to generate qrcode
        error_correction_order (int): how many errors can be corrected
        version (int, optional): _description_. Defaults to 1.

    Return:
        str: reminding message
    """

    # Generate QR code
    qr = qrcode.QRCode(
        version=version,
        error_correction=li_error_correction[error_correction_order],
        box_size=10,
        border=4)
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    # Save the image
    img.save(abspath("./qrcode.png"))

    return "QR code has been saved to 'qrcode.png', which is in the current folder."
