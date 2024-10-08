from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI 
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from LlamaIndex_Pdf import pdf_engine 
import os 


# Another method of direectly using your api key 
os.environ["OPEN_AI_API_KEY"] = "ENTER YOUR API KEY"
api_key=os.environ["OPEN_AI_API_KEY"]


tools = [
    QueryEngineTool(
        query_engine=pdf_engine,
        metadata=ToolMetadata(
            name="Name you want to set for your pdf",
            description="Detailed description about your pdf",
        ),
    ),
]

llm=OpenAI(api_key=api_key, model="gpt-3.5-turbo-0613")
agent= ReActAgent.from_tools(tools, llm=llm, verbose = True)
