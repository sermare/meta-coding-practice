from problems.p678_longest_absolute_file_path import solution

TEST_CASES = [
    {
        "description": "Basic file path",
        "run": lambda: solution("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"),
        "expected": 20,
    },
    {
        "description": "Nested deeper",
        "run": lambda: solution("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"),
        "expected": 32,
    },
    {
        "description": "No file (no dot)",
        "run": lambda: solution("dir\n\tsubdir1\n\tsubdir2"),
        "expected": 0,
    },
    {
        "description": "Single file at root",
        "run": lambda: solution("file.txt"),
        "expected": 8,
    },
]
