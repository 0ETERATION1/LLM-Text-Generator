import fitz  # PyMuPDF
import requests
from io import BytesIO

def extract_text_from_pdf(pdf_path_or_url):
    text = ""
    
    # Check if the path is a URL
    if pdf_path_or_url.startswith('http://') or pdf_path_or_url.startswith('https://'):
        # The path is a URL, download the PDF data
        response = requests.get(pdf_path_or_url)
        response.raise_for_status()  # Ensure the request was successful
        pdf_data = BytesIO(response.content)
        doc = fitz.open("pdf", pdf_data)
    else:
        # The path is not a URL, assume it's a local file path
        doc = fitz.open(pdf_path_or_url)
    
    # Extract text from each page
    for page in doc:
        text += page.get_text()
    doc.close()
    
    return text
