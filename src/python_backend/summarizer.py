# src/python_backend/summarizer.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the API key from an environment variable

def summarize_text(text, prompt_template, model="text-davinci-003", max_tokens=150):
    """
    Summarizes the given text using OpenAI's GPT model.
    I think we could play around with different engines. 4.5 turbo seems very useful for CLI purposes

    Parameters:
        text (str): The text to summarize.
        model (str): The OpenAI GPT model to use for summarization.
        max_tokens (int): The maximum number of tokens to generate in the summary.

    Returns:
        str: The summarized text.
    """
    
    # Replace placeholder text with the actual input text
    prompt = prompt_template.replace("TEXT", text)
    
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,  # Use the modified prompt here
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"An error occurred during text summarization: {e}")
        return "An error occurred during summarization."

def test_summarize_text():
    test_text = "OpenAI's GPT-3 is a state-of-the-art language processing AI model designed to understand and generate natural language. It can answer questions, write essays, summarize texts, and even create code based on the description provided."
    prompt_template = "Summarize this text: TEXT"
    
    summary = summarize_text(test_text, prompt_template, model="text-davinci-003", max_tokens=100)
    
    print("Original Text:", test_text)
    print("\nGenerated Summary:", summary)
    
    assert summary != "", "The summary should not be empty."

# Example usage
# Corrected example usage in summarizer.py

if __name__ == "__main__":
    example_text = "Your text to summarize goes here."
    prompt_template = "Summarize this text: TEXT"  # Define a prompt template

    # Now call summarize_text with both required arguments
    print(summarize_text(example_text, prompt_template))

    # Running the test
    print("\nRunning test_summarize_text...")
    test_summarize_text()


#TASK: TL;DR/SUMMARY of TEXT in JSON. JSON keys: "titles" (array of strings): 2-5 appropriate titles for TEXT; "tags" (string): tag cloud; 
# "entities" (array of {"name", "description"} objects): named entities, including persons, organizations, processes, etc. their detailed description and relationships;
# "short_summaries" (array of strings): one-two sentence summaries of TEXT; "style" (string): type, sentiment and writing style of TEXT; "arguments" (array of strings):
# 5-10 main arguments of TEXT; "summary" (string): detailed summary of TEXT