from PyPDF2 import PdfReader
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import io
import streamlit as st
load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    print("start of pdf reading")
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)  # Wrap in BytesIO
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    print("end of pdf reading")
    return text

def get_text_chunks(text):
    print("start of text splitting")
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    chunks=text_splitter.split_text(text)
    print("end of text splitting")
    return chunks

def get_vector_store(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template="""
    Answer the question as detailed as possible from the provided context,make sure to provide all the details,if the answer is not available
    in provided context just say,"answer is not available in the context",dont provide the wrong answer
    Context:\n{context}?\n
    Question:\n{question}\n
    
    Answer:
    """

    model=ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.3)
    prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
    chain = load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain

def user_input(user_question):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain=get_conversational_chain()
    response = chain(
        {"input_documents":docs,"question":user_question}
        ,return_only_outputs=True
    )

    print(response)
    st.write("Reply: ",response["output_text"])

def main():
    st.set_page_config("Chat with multiple PDF")
    st.header("Chat with multiple PDF using Gemini")

    user_question = st.text_input("Ask a question from pdf files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the submit & Process",accept_multiple_files=True)
        print(type(pdf_docs),pdf_docs)
        if st.button("Submit & Process"):
            with st.spinner("Processing...."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()