# src/python_backend/summarizer.py
import os
import openai

# Load the API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

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
            # TODO: Change the prompt to better suit the summarization task
            # OpenAI has a variety of prompt engineering adive we can look into
            prompt=f"Summarize this text: {text}",
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

# Example usage
if __name__ == "__main__":
    example_text = "Your text to summarize goes here."
    print(summarize_text(example_text))


#TASK: TL;DR/SUMMARY of TEXT in JSON. JSON keys: "titles" (array of strings): 2-5 appropriate titles for TEXT; "tags" (string): tag cloud; 
# "entities" (array of {"name", "description"} objects): named entities, including persons, organizations, processes, etc. their detailed description and relationships;
# "short_summaries" (array of strings): one-two sentence summaries of TEXT; "style" (string): type, sentiment and writing style of TEXT; "arguments" (array of strings):
# 5-10 main arguments of TEXT; "summary" (string): detailed summary of TEXT