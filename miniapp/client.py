# import streamlit as st
# from typing import Literal
# from dataclasses import dataclass
# import requests

# #streamlit

# @dataclass
# class Message:
#     """Class for keeping track of a chat message"""
#     origin: Literal["human", "chatbot"]
#     message: str

# def on_click_callback():
#     human_prompt = st.session_state.human_prompt
#     messages = st.session_state.template_messages
#     messages.append(("human", "{human_prompt}"))

#     response = requests.post(
#         "http://localhost:8080/exposition/invoke",
#         json={"input":{"concept":concept, "audience":audience}},
#     )
#     llm_response = response.json()["output"]

#     st.session_state.history.append(
#         Message("human", human_prompt)
#     )
#     st.session_state.history.append(
#         Message("chatbot", llm_response)
#     )
#     st.session_state.template_messages.append(("human",human_prompt))
#     st.session_state.template_messages.append(("system",llm_response))

# def initialize_session_state():
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "template_messages" not in st.session_state:
#         st.session_state.template_messages = [("system", chat_bot_prompt)]

# initialize_session_state()

# st.title("Pizza parlor!!!")

# chat_placeholder = st.container()
# prompt_placeholder = st.form("chat-form")

# with chat_placeholder:
#     for chat in st.session_state.history:
#         st.markdown(f"*{chat.origin}*: {chat.message}")

# with prompt_placeholder:
#     st.markdown("**Chat** - _press Enter to Submit_")
#     cols = st.columns((6,1))
#     cols[0].text_input(
#         "Chat",
#         label_visibility="collapsed",
#         key="human_prompt",
#     )
#     cols[1].form_submit_button(
#         "Submit",
#         type="primary",
#         on_click=on_click_callback
#     )