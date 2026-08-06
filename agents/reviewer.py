from tools.python_tool import execute_python
from llm import llm
from langchain_core.prompts import ChatPromptTemplate

with open("prompts/reviewer_prompt.txt", "r", encoding="utf-8") as file:
    reviewer_prompt = file.read()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", reviewer_prompt)
    ]
)

chain = prompt | llm


def review_code(code: str):

    execution_result = execute_python(code)

    response = chain.invoke(
        {
            "code": code,
            "success": execution_result.success,
            "output": execution_result.output,
            "error": execution_result.error,
        }
    )

    return response.content