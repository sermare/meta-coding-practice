from problems.p847_unique_binary_search_trees import solution

TEST_CASES = [
    {
        "description": "n=3: 5 unique BSTs",
        "run": lambda: solution(3),
        "expected": 5,
    },
    {
        "description": "n=1: 1 BST",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n=4: 14 BSTs",
        "run": lambda: solution(4),
        "expected": 14,
    },
    {
        "description": "n=5: 42 BSTs",
        "run": lambda: solution(5),
        "expected": 42,
    },
]
