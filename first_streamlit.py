import streamlit as st
st.title('Hello There!')
# Markdown
st.markdown('Welcome to my first streamlit app')

# colored text success -  green
st.success('Congratulations')

st.sidebar.title('Menu')

st.sidebar.button('Chatbot')
st.sidebar.button('About Us')

prompt = st.text_area("Prompt: ", placeholder='Ask me anything...', height=50)
submit = st.button('Submit')