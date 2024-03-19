from langchain_community.llms import GooglePalm
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS 
# import google.generativeai as palm
from langchain_google_genai import GoogleGenerativeAI

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.1)

instructor_embeddings = HuggingFaceInstructEmbeddings()
vector_db_path = "faiss_index"
# use function so you dont have to run the create db code everytime
def create_vector_db() :

    loader = CSVLoader(file_path = 'codebasics_faqs.csv', source_column= 'prompt')
    data = loader.load()
    vectorDB = FAISS.from_documents(documents = data, embedding = instructor_embeddings)
    vectordb.save_local(vector_db_path)


if __name__ == "__main__" :
    create_vector_db()