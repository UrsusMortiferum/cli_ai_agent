from functions.run_python_file import run_python_file

TEST_CASES = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt"),
]


def _run_and_print(working_directory: str, file_path: str, args: None):
    if args is None:
        args = []
    print(f"Running '{file_path}' in '{working_directory}' directory with args: {args}")
    print(run_python_file(working_directory, file_path, args))
    print("")


def test():
    for case in TEST_CASES:
        working_directory, file_path, *rest = case
        args = rest[0] if rest else None

        _run_and_print(working_directory, file_path, args)


if __name__ == "__main__":
    test()
