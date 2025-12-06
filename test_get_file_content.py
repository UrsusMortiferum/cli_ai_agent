from functions.get_file_content import get_file_content

TEST_CASES = [
    ("Result for 'main.py'", "calculator", "main.py"),
    ("Result for 'pkg/calculator.py' directory:", "calculator", "pkg/calculator.py"),
    ("Result for '/bin/cat' directory:", "calculator", "/bin/cat"),
    (
        "Result for 'pkg/does_not_exist.py' directory:",
        "calculator",
        "pkg/does_not_exist.py",
    ),
]


def _run_and_print(label: str, working_directory: str, file_path: str) -> None:
    print(label)
    print(get_file_content(working_directory, file_path))
    print("")


def test() -> None:
    for label, working_directory, file_path in TEST_CASES:
        _run_and_print(label, working_directory, file_path)


if __name__ == "__main__":
    test()
