#from openai import OpenAI
from mistralai import Mistral
import streamlit as st

with st.sidebar:
    api_key = st.text_input("Mistral API Key", key="chatbot_api_key", type="password")
    "您可以去Mistral官网申请API"
    "[获得一个API](https://docs.mistral.ai/)"
st.title("💬 聊天机器人")
st.caption("🚀 通过Streamlit和Mistral构建的")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "我可以帮您做什么?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("请输入Mistral的api，然后继续")
        st.stop()

    client = Mistral(api_key=api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.complete(model="mistral-large-latest", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)