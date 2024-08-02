# PDF Data Masking Application

## Objective
Develop a robust application that masks sensitive information from input PDFs, ensuring data privacy and security. The application must handle text and images within the PDF, accommodating diverse names across different demographics, including Malaysian, Chinese, and Korean names.

## Requirements
- Input: PDF files containing customer-sensitive information such as names, phone numbers, email addresses, and clinic names.
- Output: A new PDF file with all sensitive information masked or removed.

## Features
1. Text Extraction and Masking
2. Image Processing
3. Multi-language Support
4. Performance
   - Efficient processing to handle large PDFs and multiple files simultaneously.
   - Ensure accuracy in identifying and masking sensitive information.
5. API Integration (Gemini API)
6. Frontend for file upload and download

## Technologies Used
- Python
- PyPDF2
- pdfminer.six
- Pillow
- pytesseract
- opencv-python
- pandas
- langdetect
- spaCy
- Flask
- requests
- fitz

## Installation
1. Clone the repository.
2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env\Scripts\activate
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
4. Download the spaCy model:
    ```sh
    python -m spacy download en_core_web_sm
    ```

## Usage
1. Start the Flask application:
    ```sh
    python src/app.py
    ```
2. Open a web browser and go to `http://127.0.0.1:5000`.
3. Upload a PDF file and download the processed file.

## Configuration
- The paths for the input and output PDF files are configured in `src/config.py`.

## Deliverables
1. Source code of the application.
2. Documentation on how to set up and run the application.
3. A demo video showing the application in action.
