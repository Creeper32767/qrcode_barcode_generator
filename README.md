# QR & Barcode Generator

<div align="center">

A versatile desktop tool for generating and analyzing QR codes and various barcode formats.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Creeper32767/qrcode_barcode_generator/pulls)

</div>

<p align="center">
  <img src="./src/qrcode.png" alt="QR Code Example" width="400">
  <img src="./src/barcode.png" alt="Barcode Example" width="400">
</p>

## About The Project

**QR & Barcode Generator** is a Python-based application that simplifies the creation and decoding of various 1D and 2D codes. Whether you need to generate a QR code for a URL, a product barcode for inventory, or analyze an existing code from an image, this tool provides a straightforward solution.

### Built With

This project relies on a set of powerful open-source libraries:

*   [Python](https://www.python.org/)
*   [qrcode](https://github.com/lincolnloop/python-qrcode) (for QR Code generation)
*   [python-barcode](https://github.com/WhyNotHugo/python-barcode) (for standard barcode generation)
*   [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) (for code analysis and decoding)
*   [Pillow](https://python-pillow.org/) (for image processing)
*   [Colorama](https://github.com/tartley/colorama) (for colored terminal output)

## Features

*   **Generate QR Codes:** Quickly create QR codes from any text or data.
*   **Generate Barcodes:** Supports a wide variety of standard barcode formats, including EAN-13, Code128, and more.
*   **Analyze Codes:** Decode QR codes and barcodes directly from image files to retrieve their embedded data.
*   **Save & Export:** Save your generated codes as image files for use in other applications.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

You need to have Python and pip installed on your system.
*   **Python 3.8+**
    ```sh
    python --version
    ```

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Creeper32767/qrcode_barcode_generator.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd qrcode_barcode_generator
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```sh
    python main.py
    ```

## Usage

Once the application is running:

*   **To Generate:**
    1.  Select the option to "Generate".
    2.  Choose the desired code type (e.g., QR Code, EAN-13).
    3.  Enter the data you want to encode.
    4.  The application will generate and save the code as an image file.

*   **To Analyze:**
    1.  Select the option to "Analyze".
    2.  Provide the path to the image file containing a code.
    3.  The application will decode the code and display the embedded information.

## Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Please give the project a star if you find it useful! Thank you!

## License

Distributed under the MIT License. See `LICENSE` for more information.

Copyright © 2025 by Creeper32767

## Contact

Creeper32767 - [@Creeper32767](https://github.com/Creeper32767)

Project Link: [https://github.com/Creeper32767/qrcode_barcode_generator](https://github.com/Creeper32767/qrcode_barcode_generator)
