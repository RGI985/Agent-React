import streamlit as st
from google import genai
from dotenv import load_dotenv
from google.genai import types
import io
from gtts import gTTS

load_dotenv()
client = genai.Client()

# Streamed response emulator
def response_generator(contents):
    # Change to generate_content_stream
    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low"))
    )
    for chunk in response:
        # Check if the chunk has text before yielding
        if chunk.text:
            yield chunk.text



st.title("ChatBOT")
contents=""
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Assistant response logic
    with st.chat_message("assistant"):
        # Check if the user is asking for an image
        if "generate image" in prompt.lower() or "create image" in prompt.lower():
            response = "Currently, we don't have the facility to generate images. I can only help you with text-based questions for now!"
            st.info(response)
        else:
            # Show a spinner while the model "thinks"
            with st.spinner("Thinking..."):
                response = st.write_stream(response_generator(prompt))
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
