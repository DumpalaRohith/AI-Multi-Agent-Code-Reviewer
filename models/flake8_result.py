from pydantic import BaseModel
class Flake8Result(BaseModel):
    success: bool
    report : str