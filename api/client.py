import streamlit as st
import requests

def call_server(concept, audience):
    response = requests.post(
        "http://localhost:8080/exposition/invoke",
        json={"input":{"concept":concept, "audience":audience}},
    )

    return response.json()['output']

st.title("Exposition application")
audience = ["Child","Teen","College Student","Grad Student", "Expert"]

concept_input = st.text_input("What do you want to know?")
audience_option = st.radio(
    label="How well do you want your explanation to be? It should be understood by:",
    options=audience,
)

if concept_input:
    st.write(call_server(concept=concept_input, audience=audience_option))