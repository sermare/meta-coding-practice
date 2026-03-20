from problems.p848_unique_binary_search_trees_ii import solution

TEST_CASES = [
    {
        "description": "n=3: 5 unique BSTs",
        "run": lambda: len(solution(3)),
        "expected": 5,
    },
    {
        "description": "n=1: 1 BST",
        "run": lambda: len(solution(1)),
        "expected": 1,
    },
    {
        "description": "n=2: 2 BSTs",
        "run": lambda: len(solution(2)),
        "expected": 2,
    },
    {
        "description": "n=4: 14 BSTs",
        "run": lambda: len(solution(4)),
        "expected": 14,
    },
]
