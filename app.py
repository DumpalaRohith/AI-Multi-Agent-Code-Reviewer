from agents.reviewer import review_code
from agents.optimizer import optimize_code 
from agents.explainer import explain_changes
sample_code = """
a = [1,2,3]

for i in range(len(a)):
    print(a[i])
"""
from workflow import workflow

result=workflow.invoke(
    {
        "code":sample_code,
        "review":"",
        "optimized_code":"",
        "explanation":""
    }
)
print("=========REVIEW=========")
print(result["review"])
print("\n=========OPTIMIZED CODE==========")
print(result["optimized_code"])
print("\n=========EXPLANATION============")
print(result["explanation"])
