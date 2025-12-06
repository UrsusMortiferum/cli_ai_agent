from functions.get_files_info import get_files_info

TEST_CASES = [
    ("Result for current directory:", "calculator", "."),
    ("Result for 'pkg' directory:", "calculator", "pkg"),
    ("Result for '/bin' directory:", "calculator", "/bin"),
    ("Result for '../' directory:", "calculator", "../"),
]


def _run_and_print(label: str, working_directory: str, directory: str) -> None:
    print(label)
    print(get_files_info(working_directory, directory))
    print("")


def test() -> None:
    for label, working_directory, directory in TEST_CASES:
        _run_and_print(label, working_directory, directory)


if __name__ == "__main__":
    test()
