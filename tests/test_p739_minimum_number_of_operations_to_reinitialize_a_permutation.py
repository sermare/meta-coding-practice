from problems.p739_minimum_number_of_operations_to_reinitialize_a_permutation import solution

TEST_CASES = [
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": 1,
    },
    {
        "description": "n=4",
        "run": lambda: solution(4),
        "expected": 2,
    },
    {
        "description": "n=6",
        "run": lambda: solution(6),
        "expected": 4,
    },
    {
        "description": "n=8",
        "run": lambda: solution(8),
        "expected": 3,
    },
]
