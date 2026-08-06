from llm import llm
from langchain_core.prompts import ChatPromptTemplate
with open("prompts/explainer_prompt.txt", "r") as file:
    explainer_prompt = file.read()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",explainer_prompt),
        (
            "human",
            """
            Orginal Code:
            {code}
            Review Report:
            {review}
            Optimized Code:
            {optimized_code}
            """
            
        )
    ]
)
chain=prompt | llm
def explain_changes(
    code:str,
    review:str,
    optimized_code:str
):
    response = chain.invoke(
        {
            "code":code,
            "review":review,
            "optimized_code":optimized_code
        }
    )
    return response.content