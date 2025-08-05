import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    # if not abs_file_path[-3:] == ".py":
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            #     ["uv", "run", file_path] + args,
            commands,
            capture_output=True,
            cwd=abs_working_dir,
            timeout=30,
            text=True,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."

        # stdout, stderr, return_code = result.stdout, result.stderr, result.returncode
        # output = ""
        # output += f"STDOUT:\n{stdout}"
        # output += f"STDERR:\n{stderr}"
        # if return_code != 0:
        #     output += f"Process exited with code {return_code}"
        # if stdout == "":
        #     output = "No output produced"
        # return output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file with provided args, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to python file to be executed, relative to the working directory. If not provided, returns an error.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Additional args for execution of script. If not provided, no args will be considered.",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)
