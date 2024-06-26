import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# loading response json format
with open('C:\\Users\\minhh\\mcqgen\\Response.json') as file:
    RESPONSE_JSON = json.load(file)
    
# creating a title for the app
st.title("MCQs Creator Application with LangChain")

# Create a form using st.form
with st.form("user_inputs"):
    # File Upload 
    uploaded_file = st.file_uploader("Upload a PDF or txt file")
    
    # Number of questions
    mcq_count = st.number_input("Number of questions", 
                                min_value = 3, 
                                max_value = 50)
    
    # Subject
    subject = st.text_input("Insert subject", max_chars= 20)
    
    # Quiz tone
    tone = st.text_input("Complexity Level Of Questions",
                         max_chars= 20, 
                         placeholder= "Simple")
    
    # Add button
    button = st.form_submit_button("Create Multiple Choice Questions")
    
    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                # Count tokens and the cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    })
                    
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
            
            else:
                print(cb)
                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            # Display the review in  a text box as well
                            st.text_area(label="Review", value=response.get("review"))
                        else:
                            st.error("Error in the table data")
                    else:
                        st.write(response)