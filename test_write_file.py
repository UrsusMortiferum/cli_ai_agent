from functions.write_file import write_file


TEST_CASES = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]


def _run_and_print(working_directory: str, file_path: str, content: str):
    print(f"Result for '{file_path}' in '{working_directory}' directory:")
    print(write_file(working_directory, file_path, content))
    print("")


def test():
    for working_directory, file_path, content in TEST_CASES:
        _run_and_print(working_directory, file_path, content)


if __name__ == "__main__":
    test()
