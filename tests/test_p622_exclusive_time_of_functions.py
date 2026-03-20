from problems.p622_exclusive_time_of_functions import solution

TEST_CASES = [
    {
        "description": "Two functions nested",
        "run": lambda: solution(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]),
        "expected": [3, 4],
    },
    {
        "description": "Single function",
        "run": lambda: solution(1, ["0:start:0", "0:end:0"]),
        "expected": [1],
    },
    {
        "description": "Sequential functions",
        "run": lambda: solution(2, ["0:start:0", "0:end:2", "1:start:3", "1:end:5"]),
        "expected": [3, 3],
    },
    {
        "description": "Recursive calls",
        "run": lambda: solution(1, ["0:start:0", "0:start:2", "0:end:5", "0:end:6"]),
        "expected": [7],
    },
]
