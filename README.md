# Text-Generation

**Group members**: Kevin Liao, Alex Terskin, Sean Sweeney, Faadil Shaikh, Rodrigo Sandon
**Project 9**: Using an LLM API to summarize text.

# Project Description
Our group will build a design LLM that will have the ability to summarize text.
Currently, the goal is for the program to be able to read in a document that is given from the
user’s file system, which will most likely be in a pdf format. Parse out the paper and summarize
it in the best way possible. Focusing on key points, arguments, and conclusions from the given
text. Our program would also need to be proficient at ignoring unnecessary filler text and
identifying relevant information for proper summarization. To achieve this, we would have to
implement a way to train our model. We would have to feed large amounts of data into our
system to ensure it can properly summarize from a variety of sources. Our goal is to build a
simple yet effective summarization tool that can be used for students. As well as making it free.

**Features**:
- Able to read documents and Pdfs and summarize their contents.
- (Optional) Be able to do the same through video and audio files.

**Deliverables**:
- A command line tool with various input and output options and flags.
- May extend it to a simple web app

**Format**:
- Likely to use Python to write the code to build the model.
- Probably use ChatGPT API as LLM
- Training of the model will also likely be done in Python, but data will come from external
sources.
- We will also likely provide a write up of our project as a whole, what it means to
accomplish, and the final results concerning the efficacy of the model.

**IMPORTANT**
- Before running the python code, install the following dependencies:
    pip3 install requests
    pip3 install selenium
    pip3 install webdriver-manager
    pip3 install beautifulsoup4
- Use the following command to install the OpenAI API: 
    pip3 install --upgrade openai
- CLI tool uses argparse to build out options and interface

**TESTING**
- Testing is assisted by pytest
    pip3 install pytest
    