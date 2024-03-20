import streamlit as st 
from langChainHelper import create_vector_db, get_qa_chain 


st.title("CodeBasics QA")
btn = st.button("Create Knowledge Database")

if btn :
    pass

question = st.text_input("Question")

if question :
    chain = get_qa_chain()
    response = chain(question)
    st.header("Answer: ")
    st.write(response["result"])
