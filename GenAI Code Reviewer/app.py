import streamlit as st
import google.generativeai as genai

f = open("/content/code.txt")
key = f.read()
genai.configure(api_key="AIzaSyBZupEqXpoSulCx-dRy8bGly8Sk4W8PvlE")

system_prompt ="""
You are an AI Python Tutor. Check the provided code. If it's correct, say, 'The code is correct.' If there's a bug, provide a bug report and fixed code.
"""
model = genai.GenerativeModel(model_name = 'gemini-1.5-flash',system_instruction=system_prompt)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("/content/image-removebg-preview.png", width=100)

st.title("🔍 Python Code Review Assistant")
st.markdown(
    "<h3 style='font-size:18px; color: #333; text-align:center;'>Submit your Python code for review and receive detailed feedback.</h3>",
    unsafe_allow_html=True)


# Sidebar for instructions
st.sidebar.title("📋 Instructions")
st.sidebar.write(
    """
    1. Paste your Python code into the editor below.
    2. Click the "Review Code" button to analyze your code.
    3. Receive detailed feedback, bug identification, and suggested fixes.
    """
)
st.markdown(
    """
    <style>
    .stTextArea textarea {
        background-color: #f0f0f0;
        color: black;
        border: 1px solid #ccc;
    }
        .stButton>button {
        background-color: #80b3ff; 
        color: black;  
        border: none; 
    }
        .stButton > button:active {
        background-color: #ff6666; 
    
    </style>
    """,
    unsafe_allow_html=True
)

user_prompt = st.text_area("Enter your code", placeholder="Type your code here")

btn_click = st.button("Review Code")

if btn_click == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
