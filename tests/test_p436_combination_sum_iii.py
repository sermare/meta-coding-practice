from problems.p436_combination_sum_iii import solution

TEST_CASES = [
    {
        "description": "k=3 n=7",
        "run": lambda: solution(3, 7),
        "expected": [[1, 2, 4]],
    },
    {
        "description": "k=3 n=9",
        "run": lambda: sorted(solution(3, 9)),
        "expected": sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    },
    {
        "description": "k=4 n=1 (impossible)",
        "run": lambda: solution(4, 1),
        "expected": [],
    },
    {
        "description": "k=2 n=3",
        "run": lambda: solution(2, 3),
        "expected": [[1, 2]],
    },
    {
        "description": "k=1 n=5",
        "run": lambda: solution(1, 5),
        "expected": [[5]],
    },
]
