from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "sarcastic_bot"

# build a LLM chain
promptTemplate = ChatPromptTemplate.from_messages(
    [
        ("system", "Reply with {way} to all the questions"),
        ("user", "Question:{question}"),
    ]
)

model = ChatGroq(model="mixtral-8x7b-32768")
parser = StrOutputParser()

chain = promptTemplate|model|parser

#create streamlit
st.title("Sarcastic GROQ")
input_text = st.text_input("Ask you question mate!")

if input_text:
    st.write(chain.invoke({"way": "sarcasm", "question": input_text}))