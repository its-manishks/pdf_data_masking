# src/extract_images.py
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    images = []

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(image_bytes)

    return images
