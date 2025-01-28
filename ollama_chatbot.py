import streamlit as st
from config import Config
from helpers.llm_helper import chat, stream_parser
import ollama

# Initialize client once and store it in session state
if "client" not in st.session_state:
    st.session_state.client = ollama.Client(host=Config.host)

client = st.session_state.client

# Set page config with wide layout
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    layout="wide",  # Enable wide layout
    initial_sidebar_state="expanded"
)


# Check if the greeting message has been added to session state, if not, add it
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey there! 👋 I'm Lucy, your personal assistant. How can I help you today?"}]

st.title(Config.PAGE_TITLE)

# Set up sidebar navigation widgets
with st.sidebar:
    st.markdown("# Chat Options")
    model = st.selectbox('What model would you like to use?', Config.OLLAMA_MODELS)

# Display chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What would you like to ask?"):
    # Display user prompt in chat message widget
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Add user's prompt to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner('Generating response...'):
        # Retrieve response from model
        llm_stream = chat(user_prompt, model=model, client=client)

        # Stream the response back to the screen
        stream_output = st.write_stream(stream_parser(llm_stream))

        # Append response to the message list
        st.session_state.messages.append({"role": "assistant", "content": stream_output})
