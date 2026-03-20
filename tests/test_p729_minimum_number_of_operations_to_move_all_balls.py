from problems.p729_minimum_number_of_operations_to_move_all_balls import solution

TEST_CASES = [
    {
        "description": "Basic case: '110'",
        "run": lambda: solution("110"),
        "expected": [1, 1, 3],
    },
    {
        "description": "Single ball: '001011'",
        "run": lambda: solution("001011"),
        "expected": [11, 8, 5, 4, 3, 4],
    },
    {
        "description": "All zeros: '000'",
        "run": lambda: solution("000"),
        "expected": [0, 0, 0],
    },
    {
        "description": "Single box with ball: '1'",
        "run": lambda: solution("1"),
        "expected": [0],
    },
]
