import streamlit as st
from openai import OpenAI

st.title("LLM 웹 앱")

# API Key session_state 저장
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    value=st.session_state.api_key
)

st.session_state.api_key = api_key


# 캐시 사용
@st.cache_data
def get_response(question, api_key):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content


question = st.text_input("질문 입력")

if st.button("전송"):
    answer = get_response(question, api_key)
    st.write(answer)
