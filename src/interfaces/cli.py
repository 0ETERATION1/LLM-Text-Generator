# src/interfaces/cli.py
import argparse
from src.python_backend.controller import process_input

def main():
    parser = argparse.ArgumentParser(description="Universal Text Summarization Tool")
    parser.add_argument("text", nargs='?', default="", help="Direct text to summarize")
    parser.add_argument("--file", help="Path to a local text or PDF file", type=str)
    parser.add_argument("--url", help="URL of the web page to summarize", type=str)
    parser.add_argument("-v", "--verbose", help="Gives verbose summary", action='store_true')
    parser.add_argument("--tldr", help="Gives a quick and concise summary of key points", action='store_true')
    parser.add_argument("--json", help="Gives a JSON representation of the summary key points", action='store_true')
    parser.add_argument("--titles", help="Gives the user a list of possible headlines for the text", action='store_true')
    args = parser.parse_args()

    # Decide on the summary type based on flags provided
    summary_type = "simple_summary"  # Default
    if args.verbose:
        summary_type = "detailed_summary"
    elif args.tldr:
        summary_type = "short_summary"
    elif args.json:
        summary_type = "json_summary"
    elif args.titles:
        summary_type = "titles_summary"

    if args.text:
        input_type = "text"
        content = args.text
    elif args.file:
        input_type = "file"
        content = args.file
    elif args.url:
        input_type = "url"
        content = args.url
    else:
        # If no input is provided, prompt the user for text input
        content = input("Please enter the text you want to summarize: ")
        input_type = "text"
    
    summary = process_input(input_type=input_type, content=content, summary_type=summary_type)
    print("Summary:", summary)

if __name__ == "__main__":
    main()


    """
    Allow users to select flags for various options
    
    -v: gives verbose summary
    -tldr: gives user quick and concise summary of key points
    -json: gives user a json representation of the summary key points
    -titles: gives the user a list of possible headlines for the text
    
    Example Usage:
    
    # Summarize text directly with a verbose summary
    python cli.py "Here is some text that I want to summarize in detail." --verbose

    # Summarize text from a file with a concise summary (TL;DR)
    python cli.py --file /path/to/document.txt --tldr

    # Summarize web content with JSON key points
    python cli.py --url "https://example.com/article" --json

    # Get possible headlines for the direct text
    python cli.py "This is another piece of text for which I need headlines." --titles
    
    """

