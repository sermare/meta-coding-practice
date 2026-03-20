from problems.p311_insert_delete_getrandom_o1 import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(
            ["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
            [[1], [2], [2], [], [1], [2], []]
        ),
        "expected": [True, False, True, 2, True, False, 2],
    },
    {
        "description": "Insert duplicates",
        "run": lambda: solution(["insert", "insert"], [[1], [1]]),
        "expected": [True, False],
    },
    {
        "description": "Remove non-existent",
        "run": lambda: solution(["remove"], [[1]]),
        "expected": [False],
    },
    {
        "description": "Insert and remove same",
        "run": lambda: solution(["insert", "remove", "insert"], [[1], [1], [1]]),
        "expected": [True, True, True],
    },
]
