import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from openai import OpenAI  # import OpenAI API

# sets up calls to OpenAI API
client = OpenAI(
    api_key="sk-proj-1hikOI9r55lLJ0ZPY9pOT3BlbkFJgKn3mcR5caCeQ4Nz1nyA")

# push to commit new API key


def get_all_text_with_javascript(url):

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # This DOES NOT open up browser
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    body_text = driver.find_element(By.TAG_NAME, "body").text.splitlines()
    cleaned_text = '\n'.join(line.strip()
                             for line in body_text if line.strip())

    driver.quit()

    print(cleaned_text)

    return cleaned_text


""" Summarizes a given text using the OpenAI API """


def summarize_text(text, max_tokens=10000):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": text}],
            model="gpt-3.5-turbo-16k",
            # prompt=text, # text to be summarized
            max_tokens=max_tokens,  # max number of tokens
            temperature=0.5,  # randomness - lower value means output is more deterministic
            top_p=1.0,  # more diverse outputs
            frequency_penalty=0.0,  # controls the repetitiveness
            presence_penalty=0.0,  # controls the repetitiveness
        )

        print("Response from API:", response)

        if response.choices[0].message.content:
            return response.choices[0].message.content
        else:
            print("No choices found in response.")
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None


def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


# Replace with the URL you want to scrape
# url = 'https://www.cs.umd.edu/'
# url = 'https://www.youtube.com/'
url = 'https://www.bbc.com/'


# calling the function
text = get_all_text_with_javascript(url)
# print(text)

summary = summarize_text(text)
print("Summary:")
print(summary)

# scraping from a file on our local computer file system
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     courses_html_tags = soup.find_all('h5')
#     for course in courses_html_tags:
#         print(course.text)
