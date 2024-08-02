import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def extract_text_positions(pdf_path, lang='eng'):
    doc = fitz.open(pdf_path)
    text_positions = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        ocr_result = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, lang=lang)
        n_boxes = len(ocr_result['level'])
        for i in range(n_boxes):
            (x, y, w, h) = (ocr_result['left'][i], ocr_result['top'][i], ocr_result['width'][i], ocr_result['height'][i])
            text = ocr_result['text'][i]
            if text.strip():  # Avoid empty text results
                text_positions.append((text, x, y, w, h))

    return text_positions
