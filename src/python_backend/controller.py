# src/python_backend/controller.py
import json
import os
from ..scrapers.pdf_scraper import extract_text_from_pdf
from ..scrapers.web_scraper import get_all_text_with_javascript
from .summarizer import summarize_text

def load_prompt_templates():
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompt_templates.json')
    with open(config_path, 'r') as file:
        templates = json.load(file)
    return templates

def process_input(input_type, content, summary_type):
    templates = load_prompt_templates()
    prompt_template = templates.get(summary_type, {}).get('prompt', 'Summarize this text: ')

    if input_type == "text":
        text_to_summarize = content
    elif input_type == "file":
        if content.endswith('.pdf'):
            text_to_summarize = extract_text_from_pdf(content)
        else:
            with open(content, 'r', encoding='utf-8') as file:
                text_to_summarize = file.read()
    elif input_type == "url":
        text_to_summarize = get_all_text_with_javascript(content)
    
    summary = summarize_text(text_to_summarize, prompt_template)
    return summary
