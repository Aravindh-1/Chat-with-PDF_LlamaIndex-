from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI 
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from LlamaIndex_Pdf import pdf_engine 
import os 

# Create a .env file and add your OpenAI api key there, thereby the model can be accessed.
load_dotenv()

tools = [
    QueryEngineTool(
        query_engine=pdf_engine,
        metadata=ToolMetadata(
            name="MS_Dhoni",
            description="Detailed description about Ms Dhoni",
        ),
    ),
]

llm=OpenAI(model="gpt-3.5-turbo-0613")
agent= ReActAgent.from_tools(tools, llm=llm, verbose = True)
