from llm import llm
from langchain_core.prompts import ChatPromptTemplate
with open("prompts/reviewer_prompt.txt","r")as file:
    reviewer_prompt = file.read()
    
    prompt=ChatPromptTemplate.from_messages(
        [
            ("system",reviewer_prompt),
            ("human","{code}")
        ]
        
    )
    
chain = prompt | llm
def review_code(code:str):
    response = chain.invoke({
        "code":code
    })
    return response.content
