from llm import llm
from langchain_core.prompts import ChatPromptTemplate
with open("prompts/optimizer_prompt.txt", "r") as file:
    optimizer_prompt =file.read()
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",optimizer_prompt),
        ("human",
         """
         Original Code:
         {code}
         Review Report:
         {review}
         """)
    ]
)  
chain=prompt | llm
def optimize_code(code:str,review:str):
    response = chain.invoke(
        {
            "code":code,
            "review":review
        }
    )
    return response.content