# Q&A chartbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv() # Takes Enviroment variables from .env

# Function to load OpenAI model and get responses
def get_openai_responses(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.6)
    response = llm(question)
    return response

# Initializing Streamlit Application
st.set_page_config(page_title="QuerySage")
st.header("QuerySage")
input_text = st.text_input("Input: ", key="input")
response = get_openai_responses(input_text)
submit = st.button("Inquire")

# If clicked Ask Button
if submit:
    st.subheader("The Response is ")
    st.write(response)
