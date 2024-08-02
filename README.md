<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgbYYh8q-lJnFL5XQjAegR-KdCTFmJz80MFQ&s" height=80>

# PDF Data Masking Application

This application provides functionality to detect and remove sensitive information from PDF files. It supports multiple languages and can process multiple PDFs simultaneously. The application also generates detailed reports showing which words were deleted and their locations.

## Features

- **Sensitive Information Detection**: Uses OCR and Named Entity Recognition to detect sensitive information such as names, phone numbers, and email addresses.
- **Multilingual Support**: Supports English, Simplified Chinese, Traditional Chinese, and Korean.
- **Batch Processing**: Can process multiple PDF files at once.
- **Detailed Reports**: Generates a detailed report after processing, showing which words were deleted and their locations.
- **Real-time Progress Updates**: Provides real-time progress updates for batch processing using Socket.IO.

## Prerequisites

1. **Python 3.7+**
2. **pip** (Python package installer)
3. **Tesseract OCR**: Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

Ensure that Tesseract is added to your system's PATH.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/pdf-data-masking.git
    cd pdf-data-masking
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Create necessary directories**:
    ```bash
    mkdir data
    mkdir data/input
    mkdir data/output
    mkdir reports
    ```

## Configuration

Create a `config.py` file in the `src` directory with the following content:

```python
INPUT_PDF_PATH = 'data/input/input.pdf'
OUTPUT_PDF_PATH = 'data/output/output.pdf'
```

## Running the Application

1. **Run the Flask application:**:
    ```bash
    python src/app.py
    ```
2. **Open your web browser and navigate to http://127.0.0.1:5000**

## Usage

## Single File Upload

1. **Select a PDF file to upload.**
2. **Choose the language of the PDF.**
3. **Optionally, enter custom sensitive words/patterns separated by commas.**
4. **Click "Upload".**

## Multiple Files Upload

1. **Select multiple PDF files to upload.**
2. **Choose the language of the PDFs.**
3. **Optionally, enter custom sensitive words/patterns separated by commas.**
4. **Click "Upload Multiple".**

## Reports

- **After processing, detailed reports showing the deleted words and their locations will be generated and saved in the `reports` directory.**

## Troubleshooting

- Ensure Tesseract is installed and added to your system's PATH.
- Verify that all required Python packages are installed using `pip list`.





