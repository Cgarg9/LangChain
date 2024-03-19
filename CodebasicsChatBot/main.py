from langchain_community.llms import GooglePalm
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS 
# import google.generativeai as palm
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

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

def get_qa_chain():

    # load the db
    vectorDB = FAISS.load_local(vector_db_path, instructor_embeddings)

    # create retriever
    retriever = vectorDB.as_retriever(score_threshold=0.7)

    prompt_template = """ Given the following text and a question, generate an answer based on this context only to provide as 
        much text as possible from "response" section in the source document context without making any changes. If the answer 
        is not found in the context, kindly state "I don't know". Do not make up answers.

    CONTEXT = {context}

    QUESTION = {question}
    """

    PROMPT = PromptTemplate(
    template = prompt_template,
    input_variables = {"context", "question"},
    )

    chain = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever = retriever,
    input_key = "query",
    return_source_documents = True,
    chain_type_kwargs = {"prompt" : PROMPT}
    )

    return chain


if __name__ == "__main__" :
    chain = get_qa_chain()

    print(chain("Do you provide internship?"))