import streamlit as st

st.text_input("label", key = "api_key", type = "password")
st.session_state.api_key
