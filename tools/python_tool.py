import io
import contextlib
import traceback
from models.execution_result import ExecutionResult
def execute_python(code:str):
    
    buffer = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(buffer):
            exec(code)
        return ExecutionResult(
            success=True,
            output=buffer.getvalue(),
            error=""
        )
    except Exception:
        return ExecutionResult(
            success=False,
            output="",
            error=traceback.format_exc()
        )
        
        