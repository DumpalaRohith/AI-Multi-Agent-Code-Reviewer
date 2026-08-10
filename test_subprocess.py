import subprocess

result = subprocess.run(
    ["python", "-m", "flake8", "sample.py"],
    capture_output=True,
    text=True
)

print("STDOUT")
print(result.stdout)

print("STDERR")
print(result.stderr)

print("RETURN CODE")
print(result.returncode)