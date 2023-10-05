from langchain.prompts import PromptTemplate

def pdfreaderprompt():
    prompt_template = """Blockchain, the foundation of Bitcoin, has received extensive attentions recently. Blockchain serves as an immutable ledger which allows transactions take place in a decentralized manner. Blockchain-based applications are springing up, covering numerous fields including financial services, reputation system and Internet of Things (IoT), and so on. However, there are still many challenges of blockchain technology such as scalability and security problems waiting to be overcome. The below contexr presents a comprehensive overview on blockchain technology. 
{context}

Make sure you reply question only from the context.

{question}
"""
    return PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
