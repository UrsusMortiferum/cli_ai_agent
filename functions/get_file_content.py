import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            # One option to print message if file contains more than x characters
            # file_content = f.read(MAX_CHARS + 1)
            # message = ""
            # if len(file_content) > MAX_CHARS:
            #     message = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            # return file_content[:-1] + message
            file_content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return file_content
    except Exception as e:
        return f"Error: reading file: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file contents in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read contents from, relative to the working directory. If not provided, returns an error.",
            )
        },
    ),
)
