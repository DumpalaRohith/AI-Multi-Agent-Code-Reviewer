from tools.python_tool import execute_python

code = """
print("Hello Rohith")
"""

result = execute_python(code)

print(result)
print(result.success)
print(result.output)
print(result.error)