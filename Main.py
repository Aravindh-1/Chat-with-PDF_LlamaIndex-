import streamlit as st
from LlamaIndex_Pdf import pdf_engine
from llama_index.core.agent import ReActAgent
from Pdf_Chat import agent
from Pdf_Chat import tools
from Pdf_Chat import llm


st.title("Title name")
#Importing and declaring the name of agent from Pdf_Chat
agent= ReActAgent.from_tools(tools, llm=llm, verbose = True)
#User input to machine
user_input = st.text_input("Enter the question: ")

# If the user input is true
if user_input:
    response= agent.query(user_input)
    answer=response.response
    st.write(answer)
else:
    pass
