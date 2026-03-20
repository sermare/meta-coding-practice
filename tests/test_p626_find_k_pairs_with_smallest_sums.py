from problems.p626_find_k_pairs_with_smallest_sums import solution

TEST_CASES = [
    {
        "description": "Basic case: k=3",
        "run": lambda: solution([1, 7, 11], [2, 4, 6], 3),
        "expected": [[1, 2], [1, 4], [1, 6]],
    },
    {
        "description": "Duplicates: k=2",
        "run": lambda: solution([1, 1, 2], [1, 2, 3], 2),
        "expected": [[1, 1], [1, 1]],
    },
    {
        "description": "Single pair: k=1",
        "run": lambda: solution([1, 2], [3], 1),
        "expected": [[1, 3]],
    },
    {
        "description": "k larger than possible pairs",
        "run": lambda: solution([1], [1], 5),
        "expected": [[1, 1]],
    },
]
