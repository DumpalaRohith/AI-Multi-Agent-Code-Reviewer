from fastapi import FastAPI
from pydantic import BaseModel
from workflow import workflow
class ReviewRequest(BaseModel):
    code:str
    
app= FastAPI(
    title="AI Multi-Agent Code Reviewer",
    version ="1.0.0"
)

@app.get("/")
def home():
    return{
        "message":"AI Multi-Agent Code Reviewer API is running"
    }
@app.post("/review")
def review_code(request:ReviewRequest):
    
    result = workflow.invoke(
        {
            "code":request.code,
            "review":"",
            "optimized_code":"",
            "explanation":""
        }
    )
    return {
        "review": result["review"],
        "optimized_code":result["optimized_code"],
        "explanation":result["explanation"]
    }