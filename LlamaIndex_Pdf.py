import os
from llama_index.core import StorageContext , VectorStoreIndex, load_index_from_storage
#from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader

# Function to get the index of file passed in reader 
def get_index(data,index_name):
    index = None
    if not os.path.exists(index_name):
        print("Building it", index_name)
        index=VectorStoreIndex.from_documents(data,show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index= load_index_from_storage(
            
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

reader_path=os.path.join("data","E:\Intern AI Certs\Chat with Files using AI\MS_Dhoni.pdf")
reader=PDFReader().load_data(file=reader_path)
pdf_index=get_index(reader,"Dhoni")  # The variable passed with file path loads to function to get its Vector index. 
pdf_engine=pdf_index.as_query_engine()