import subprocess
import tempfile
import os

from models.flake8_result import Flake8Result


def run_flake8(code: str):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp:

        temp.write(code)
        temp_file = temp.name

    try:

        result = subprocess.run(
            ["python", "-m", "flake8", temp_file],
            capture_output=True,
            text=True
        )

        return Flake8Result(
            success=result.returncode == 0,
            report=result.stdout
        )

    finally:
        os.remove(temp_file)