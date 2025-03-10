# -*- coding: utf-8 -*-
"""apitravel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VDkau3ZmNlAzIFh0arPLmEYiLhsVPyII
"""

! pip install streamlit
!pip install langchain-google-genai
!pip install langchain langchain-google-genai google-generativeai

# Commented out IPython magic to ensure Python compatibility.
# %%writefile tourplanner.py
# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import JsonOutputParser
# 
# # Load API Key
# with open("/content/code.txt") as f:
#     API_KEY = f.read()
# 
# # Define AI Travel Assistant Prompt
# # Define AI Travel Assistant Prompt
# chat_template = ChatPromptTemplate(
#     messages=[
#         (
#             "system",
#             """
#             You are an AI-powered travel assistant that provides users with the best travel options from a given source to a specified destination.
#             Analyze multiple travel modes: flights, trains, buses, and cabs, and return details including:
# 
#             - Travel mode (Flight, Train, Bus, Cab)
#             - Cost (in INR, prefixed with "₹")
#             - Duration (e.g., "5 hours 30 minutes")
#             - Trip details (Maximum 50 words)
# 
#             Ensure the response is a valid JSON **list** (not an object), structured like this:
#             ```json
#             {{
#                 "travel_options": [
#                     {{
#                         "travel_mode": "Flight",
#                         "cost": "₹4500",
#                         "duration": "2 hours",
#                         "details": "Non-stop flight with free meal"
#                     }},
#                     {{
#                         "travel_mode": "Train",
#                         "cost": "₹1200",
#                         "duration": "5 hours 30 minutes",
#                         "details": "AC sleeper class available"
#                     }}
#                 ]
#             }}
#             ```
#             """
#         ),
#         ("human", "Find the best travel options from {source} to {destination}.")
#     ]
# )
# 
# # Initialize AI Model
# chat_model = ChatGoogleGenerativeAI(google_api_key=API_KEY, model="gemini-1.5-flash")
# 
# # Define Output Parser
# chat_parser = JsonOutputParser()
# 
# # Processing Chain
# chain = chat_template | chat_model | chat_parser
# 
# # Function to Fetch Travel Recommendations
# def get_travel_recommendations(source, destination):
#     try:
#         response = chain.invoke({"source": source, "destination": destination})
# 
#         # Ensure the response is in dictionary format
#         if isinstance(response, str):
#             response = chat_parser.parse(response)  # Parse using LangChain's parser
# 
#         # Extract the travel options if returned in a dictionary format
#         if isinstance(response, dict) and "travel_options" in response:
#             response = response["travel_options"]
# 
#         if isinstance(response, list) and all(isinstance(item, dict) for item in response):
#             return response  # Valid travel options
#         else:
#             return {"error": "Invalid JSON format returned by AI. Please try again."}
#     except Exception as e:
#         return {"error": f"AI response error: {str(e)}"}
# 
# 
# # Streamlit UI Setup
# st.set_page_config(page_title="AI-Powered Travel Planner", page_icon="🌍", layout="centered")
# 
# st.title("🌍 AI-Powered Travel Planner")
# st.subheader("Find the best travel options!")
# 
# # User Input Fields
# source = st.text_input("Enter Source Location", placeholder="Departure City")
# destination = st.text_input("Enter Destination Location", placeholder="Arrival City")
# 
# # Fetch and Display Travel Options
# if st.button("Find Best Travel Options", use_container_width=True):
#     if source and destination:
#         with st.spinner("Fetching travel recommendations..."):
#             result = get_travel_recommendations(source, destination)
# 
#             if isinstance(result, list):
#                 st.write("### 🚀 Recommended Travel Options:")
# 
#                 for option in result:
#                     travel_mode = option.get("travel_mode", "Unknown")
#                     cost = option.get("cost", "N/A")
#                     duration = option.get("duration", "Unknown")
#                     details = option.get("details", "No details available")
# 
#                     st.markdown(f"### ✈ {travel_mode}")
#                     st.markdown(f"💰 **Cost:** {cost}")
#                     st.markdown(f"⏳ **Duration:** {duration}")
#                     st.info(details)
#                     st.divider()
#             elif "error" in result:
#                 st.error(result["error"])
#             else:
#                 st.error("Unexpected response format. Please try again.")
#     else:
#         st.warning("⚠ Please enter both source and destination locations.")
# 
#

!npm install localtunnel
!streamlit run /content/tourplanner.py &>/content/logs.txt &
!npx localtunnel --port 8501 & curl ipv4.icanhazip.com