from problems.p101_reorder_data_in_log_files import solution

TEST_CASES = [
    {
        "description": "Mixed letter and digit logs",
        "run": lambda: solution(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]),
        "expected": ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
    },
    {
        "description": "All digit logs",
        "run": lambda: solution(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]),
        "expected": ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
    },
    {
        "description": "Letter logs with same content, sort by identifier",
        "run": lambda: solution(["b1 art can", "a1 art can"]),
        "expected": ["a1 art can", "b1 art can"],
    },
    {
        "description": "Only digit logs remain in order",
        "run": lambda: solution(["d1 1 2", "d2 3 4", "d3 5 6"]),
        "expected": ["d1 1 2", "d2 3 4", "d3 5 6"],
    },
    {
        "description": "Single letter log",
        "run": lambda: solution(["a1 hello world"]),
        "expected": ["a1 hello world"],
    },
]
