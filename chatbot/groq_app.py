from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] =  os.getenv("OPENAI_API_KEY")
#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "groq_tutorial"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit framework
st.title("Langchain demo with GROQ API")
input_text1=st.text_input("Search with the topic you want")

##GROQ LLM

llm = ChatGroq(model="mixtral-8x7b-32768", api_key="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")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text1:
    st.write(chain.invoke({'question':input_text1}))