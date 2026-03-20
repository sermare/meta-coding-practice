from problems.p302_encode_and_decode_strings import solution

TEST_CASES = [
    {
        "description": "Basic two words",
        "run": lambda: solution(["hello", "world"]),
        "expected": ["hello", "world"],
    },
    {
        "description": "Empty list",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Single empty string",
        "run": lambda: solution([""]),
        "expected": [""],
    },
    {
        "description": "Strings with special characters",
        "run": lambda: solution(["a#b", "c#d"]),
        "expected": ["a#b", "c#d"],
    },
    {
        "description": "Multiple empty strings",
        "run": lambda: solution(["", "", ""]),
        "expected": ["", "", ""],
    },
]
