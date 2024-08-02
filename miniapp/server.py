# from fastapi import FastAPI
# from langserve import add_routes
# import uvicorn

import streamlit as st
from typing import Literal
from dataclasses import dataclass

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# chatbot
chat_bot_prompt = "You are an excellent customer associate at a pizza place called 'Pizza parlour'.\
Your job is to attend each call from customers who want to order pizza.\
You will let them know the available pizzas at your place.\
Take into consideration the instructions from customers about ingredients and suggest them with the pizzas regulated to their instructions.\
If the user wants you to suggest a pizza, you ask them a couple questions to know their interests filter out the pizzas from the menu that they might like and will let them know.\
You will keep track of the pizzas requested by the customers in 'orders' tab.\
The customer might as well want to re-iterate through his order and remove some items from it.\
Finally, you will ask the customer to finalise the order and send it to the kitchen. You will then politely thank the customer for ordering at your place and collect his address for delivery."


template = ChatPromptTemplate
model = ChatGroq(model="gemma2-9b-it")
parser = StrOutputParser()

#streamlit

@dataclass
class Message:
    """Class for keeping track of a chat message"""
    origin: Literal["human", "chatbot"]
    message: str

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    messages = st.session_state.template_messages
    messages.append(("human", "{human_prompt}"))
    chain = template.from_messages(messages)|model|parser
    llm_response = chain.invoke({"human_prompt": human_prompt})
    st.session_state.history.append(
        Message("human", human_prompt)
    )
    st.session_state.history.append(
        Message("chatbot", llm_response)
    )
    st.session_state.template_messages.append(("human",human_prompt))
    st.session_state.template_messages.append(("system",llm_response))

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "template_messages" not in st.session_state:
        st.session_state.template_messages = [("system", chat_bot_prompt)]

initialize_session_state()

st.title("Pizza parlor!!!")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with chat_placeholder:
    for chat in st.session_state.history:
        st.markdown(f"*{chat.origin}*: {chat.message}")

with prompt_placeholder:
    st.markdown("**Chat** - _press Enter to Submit_")
    cols = st.columns((6,1))
    cols[0].text_input(
        "Chat",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit",
        type="primary",
        on_click=on_click_callback
    )