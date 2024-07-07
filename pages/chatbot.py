import streamlit as st
st.title('Chat with our bot!')

prompt = st.text_area("Prompt: ", placeholder='Ask me anything...', height=50)
submit = st.button('Submit')