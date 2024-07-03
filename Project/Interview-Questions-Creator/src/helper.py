# Importing the libraries
import os
import logging
from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
from langchain.text_splitter import TokenTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from src.prompt import *

# File processing function
def file_processing(file_path):
    # Load PDF file
    loader = PyPDFLoader(file_path)
    data = loader.load()

    question_gen = ''

    # Concatenate content from all pages
    for page in data:
        question_gen += page.page_content

    # Define a text splitter for question generation
    splitter_question_gen = TokenTextSplitter(
        model_name='gpt-3.5-turbo',
        chunk_size=10000,
        chunk_overlap=200,
    )

    # Define another text splitter for chunking
    chunk_ques_gen = TokenTextSplitter(
        model_name='gpt-3.5-turbo',
        chunk_size=10000,
        chunk_overlap=200
    )

    chunk_ques_gen = splitter_question_gen.split_text(question_gen)
    document_ques_gen = [Document(page_content=t) for t in chunk_ques_gen]

    # Define a text splitter for final splitting
    splitter_question_gen = TokenTextSplitter(
        model_name= 'gpt-3.5-turbo',
        chunk_size=1000,
        chunk_overlap=100
    )

    return document_ques_gen, document_ques_gen

# LLM pipeline function
def llm_pipeline(file_path):
    # Process the file and get document chunks
    document_ques_gen, document_answer_gen = file_processing(file_path)

    # Initialize the LLM for question generation
    llm_ques_gen_pipeline = ChatOpenAI(
        temperature=0.3,
        model='gpt-3.5-turbo'
    )

    # Define prompt templates for question generation
    PROMPT_QUESSIONS = PromptTemplate(template=prompt_template, input_variables=["text"])
    REFINE_PROMPT_QUESTIONS = PromptTemplate(template=refine_template, input_variables=["existing_answers", "text"])

    # Load question generation chain
    ques_gen_chain = load_summarize_chain(
        llm=llm_ques_gen_pipeline, 
        chain_type="refine", 
        verbose=True, 
        question_prompt=PROMPT_QUESSIONS, 
        refine_prompt=REFINE_PROMPT_QUESTIONS
    )

    # Run the chain to generate questions
    ques = ques_gen_chain.run(document_ques_gen)

    # Initialize embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(document_answer_gen, embeddings)

    # Initialize the LLM for answer generation
    llm_answer_gen = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")

    # Filter generated questions
    ques_list = ques.split("\n")
    filtered_ques_list = [element for element in ques_list if element.endswith('?') or element.endswith('.')]

    # Create answer generation chain
    answer_generation_chain = RetrievalQA.from_chain_type(
        llm=llm_answer_gen, 
        chain_type="stuff", 
        retriever=vector_store.as_retriever()
    )

    return answer_generation_chain, filtered_ques_list
