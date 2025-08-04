import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for file_name in os.listdir(abs_dir):
            file_path = os.path.join(abs_dir, file_name)
            file_size = 0
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            files_info.append(
                f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error:listing files: {e}"
