import os
from webbrowser import get


def get_files_info(working_directory, directory="."):
    if not os.path.abspath(working_directory).startswith(os.path.abspath(directory)):
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
    elif not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory')

    full_path = os.path.join(directory, working_directory)
    print(full_path)

    if directory == ".":
        directory_name = "current"
    else:
        directory_name = f"'{directory}'"

    print(f"Result for {directory_name} directory:")


get_files_info("test")
get_files_info("main.py")
get_files_info("calculator.py")
get_files_info("calculator", ".")
get_files_info("calculator", "pkg")
get_files_info("calculator", "/bin")
get_files_info("calculator", "../")
