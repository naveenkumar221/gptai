import os 
import google.generativeai as genai
import streamlit as st

os.environ["GOOGLE_API_KEY"] = "AIzaSyCf-do3xYuItW11wLxzps08oSqk9_DDo_k"


genai.configure(api_key = os.environ["GOOGLE_API_KEY"])


model = genai.GenerativeModel("gemini-1.5-pro")

def generate(input_text):
    response = model.generate_content(input_text)
    return response.text

st.title("Disney")
input_text = st.text_input("Write your prompt")
if input_text:
    st.write(generate(input_text))
    