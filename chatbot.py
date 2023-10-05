from langchain.llms import OpenAI
from src.pdfloader import load_pdf
from src.prompt import pdfreaderprompt
from langchain.chains import RetrievalQA

def CreateChatbot():
    openai_api_key = input("Input your open AI Key >>")
    vectorDB = load_pdf("C:/Users/SMRITI/Downloads/1996a557.pdf", openai_api_key)
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    prompt = pdfreaderprompt()
    chain_type_kwargs = {
        "prompt": prompt
    }
    chatbot = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorDB.as_retriever(),
        chain_type_kwargs=chain_type_kwargs
    )
    return chatbot

if __name__ == '__main__':
    chatbot = CreateChatbot()
    while (True):
        query = input("Ask Anything >> ")
        response = chatbot.run(query)
        print (response)