from extract_text import extract_text_from_pdf
from mask_info import mask_sensitive_info
from pdf_processing import delete_sensitive_info
import os

def process_pdf(input_pdf_path, output_pdf_path, lang='eng', custom_sensitive_words=None, report_path='report.txt'):
    text = extract_text_from_pdf(input_pdf_path)
    sensitive_words = mask_sensitive_info(text)
    
    if custom_sensitive_words:
        sensitive_words += custom_sensitive_words

    delete_sensitive_info(input_pdf_path, output_pdf_path, sensitive_words, lang, report_path)

def process_multiple_pdfs(input_dir, output_dir, lang='eng', custom_sensitive_words=None, report_dir='reports'):
    os.makedirs(report_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        input_pdf_path = os.path.join(input_dir, filename)
        output_pdf_path = os.path.join(output_dir, filename)
        report_path = os.path.join(report_dir, f'{filename}_report.txt')
        process_pdf(input_pdf_path, output_pdf_path, lang, custom_sensitive_words, report_path)
