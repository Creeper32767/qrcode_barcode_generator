from pyzbar import pyzbar
from PIL import Image
from os.path import abspath


def read_barcode_qrcode(image_path: str) -> list:
    """
    a function which is used to analyse barcode and qrcode

    Args:
        image_path (str): the path of barcode or qrcode image

    Returns:
        list: the information we can get from it
    """    
    # Open the image using PIL
    image = Image.open(abspath(image_path))
    # Decode the barcodes and QR codes in the image
    decoded_objects = pyzbar.decode(image)
    # Print the results
    li_result = list()
    for obj in decoded_objects:
        tup_tmp = (obj.type, obj.data.decode('utf-8'))
        li_result.append(tup_tmp)

    return li_result
