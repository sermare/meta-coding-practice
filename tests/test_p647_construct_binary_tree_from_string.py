from problems.p647_construct_binary_tree_from_string import solution

TEST_CASES = [
    {
        "description": "Standard: '4(2(3)(1))(6(5))'",
        "run": lambda: solution("4(2(3)(1))(6(5))"),
        "expected": [4, 2, 6, 3, 1, 5],
    },
    {
        "description": "Full tree: '4(2(3)(1))(6(5)(7))'",
        "run": lambda: solution("4(2(3)(1))(6(5)(7))"),
        "expected": [4, 2, 6, 3, 1, 5, 7],
    },
    {
        "description": "Negative root: '-4(2(3)(1))(6(5)(7))'",
        "run": lambda: solution("-4(2(3)(1))(6(5)(7))"),
        "expected": [-4, 2, 6, 3, 1, 5, 7],
    },
    {
        "description": "Single node: '1'",
        "run": lambda: solution("1"),
        "expected": [1],
    },
]
