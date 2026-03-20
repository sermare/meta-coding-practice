from problems.p182_evaluate_reverse_polish_notation import solution

TEST_CASES = [
    {
        "description": "(2+1)*3 = 9",
        "run": lambda: solution(["2","1","+","3","*"]),
        "expected": 9,
    },
    {
        "description": "4 + (13/5) = 6",
        "run": lambda: solution(["4","13","5","/","+"]),
        "expected": 6,
    },
    {
        "description": "Complex expression",
        "run": lambda: solution(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]),
        "expected": 22,
    },
    {
        "description": "Single number",
        "run": lambda: solution(["42"]),
        "expected": 42,
    },
]
