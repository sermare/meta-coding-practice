from problems.p623_two_sum_iii_-_data_structure_design import solution

TEST_CASES = [
    {
        "description": "Add and find existing pair",
        "run": lambda: solution(
            ["TwoSum", "add", "add", "add", "find", "find"],
            [[], [1], [3], [5], [4], [7]]
        ),
        "expected": [None, None, None, None, True, False],
    },
    {
        "description": "Find before adding",
        "run": lambda: solution(
            ["TwoSum", "find"],
            [[], [0]]
        ),
        "expected": [None, False],
    },
    {
        "description": "Duplicate adds",
        "run": lambda: solution(
            ["TwoSum", "add", "add", "find"],
            [[], [0], [0], [0]]
        ),
        "expected": [None, None, None, True],
    },
    {
        "description": "Negative numbers",
        "run": lambda: solution(
            ["TwoSum", "add", "add", "find"],
            [[], [-1], [1], [0]]
        ),
        "expected": [None, None, None, True],
    },
]
