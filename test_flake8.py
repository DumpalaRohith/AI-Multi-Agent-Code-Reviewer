from tools.flake8_tool import run_flake8

code = """
import os
import sys

a=10

print(a)
"""

result = run_flake8(code)

print(result)
print(result.success)
print(result.report)