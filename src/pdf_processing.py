import fitz  # PyMuPDF
from ocr_processing import extract_text_positions

def delete_sensitive_info(input_pdf_path, output_pdf_path, sensitive_words, lang='eng', report_path='report.txt'):
    doc = fitz.open(input_pdf_path)
    text_positions = extract_text_positions(input_pdf_path, lang)
    print(f"Text positions: {text_positions}")

    with open(report_path, 'w', encoding='utf-8') as report_file:
        report_file.write("Deleted Words Report\n")
        report_file.write("=====================\n")

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            for text, x, y, w, h in text_positions:
                if any(sensitive_word.lower() in text.lower() for sensitive_word in sensitive_words):
                    page.add_redact_annot(fitz.Rect(x, y, x + w, y + h), fill=(1, 1, 1))
                    report_file.write(f"Deleted '{text}' at ({x}, {y}, {w}, {h})\n")
                    print(f"Deleted '{text}' at ({x}, {y}, {w}, {h})")
                else:
                    print(f"Non-sensitive word '{text}' at ({x}, {y}, {w}, {h})")
            page.apply_redactions()

    doc.save(output_pdf_path)
