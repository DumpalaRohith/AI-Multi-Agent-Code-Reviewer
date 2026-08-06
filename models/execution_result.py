from pydantic import BaseModel
class ExecutionResult(BaseModel):
    success: bool
    output: str
    error: str