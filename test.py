"""
https://medium.com/@johnidouglasmarangon/how-to-summarize-text-with-openai-and-langchain-e038fc922af
"""

""" Dependencies to install:
 pip install tiktoken
 pip install langchain
"""

import urllib
import urllib.request
from langchain.chat_models import ChatOpenAI
from openai import OpenAI
from langchain.prompts import PromptTemplate
import tiktoken

url = 'https://www.cs.umd.edu/'
news_article = urllib.request.urlopen(url).read().decode("utf-8")

OPENAI_API_KEY = "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"
llm = OpenAI(api_key=OPENAI_API_KEY)

prompt_template = """Write a concise summary of the following:
{text}
CONSCISE SUMMARY IN PORTUGUESE:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

def num_tokens_from_string(string: str, encoding_name: str) -> int:    
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens = num_tokens_from_string(news_article, "text-davinci-003e")
print(num_tokens)