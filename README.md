# QR Code Generator

A simple Flask-based web application for generating QR codes. The application allows users to input text or URLs, and a corresponding QR code is dynamically generated. The QR code is then displayed on the page.

## Website is Live at: https://rasikhali.marveloussoft.tech

## Features

- Dynamic QR code generation based on user input.
- Custom color for QR codes (dark blue on white background).
- Minimalist and responsive UI design.
- Real-time QR code updates without needing a "Generate" button.

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/RasikhAli/QR-Code-Generator
    cd qr-code-generator
    ```

2. Create a virtual environment and activate it (Optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## File Structure
  ```
  QR-Code-Generator/
  │
  ├── app.py # Main Flask application
  ├── templates/
  │ └── index.html # HTML template for the application
  ├── requirements.txt # List of dependencies
  └── README.md # Project documentation
  ```


## Project Overview

### `app.py`
The main Flask application that handles routing and form submissions. It includes:
- An index route (`/`) to render the homepage and display the QR code generator form.
- The QR code generation process is handled on the server side, with custom colors applied to the QR code.

### `templates/index.html`
The HTML template that provides the user interface for the application, allowing users to input the text and generating the QR code. It features:
- A minimalist and responsive design.
- Real-time QR code updates as the user types in the input field.
- A "Clear" button to reset the input field and clear the generated QR code.


## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.
