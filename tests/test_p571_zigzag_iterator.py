from problems.p571_zigzag_iterator import solution

TEST_CASES = [
    {
        "description": "Unequal lengths: [1,2] and [3,4,5,6]",
        "run": lambda: solution([1, 2], [3, 4, 5, 6]),
        "expected": [1, 3, 2, 4, 5, 6],
    },
    {
        "description": "Short lists: [1] and [3,4]",
        "run": lambda: solution([1], [3, 4]),
        "expected": [1, 3, 4],
    },
    {
        "description": "First empty",
        "run": lambda: solution([], [1, 2, 3]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Both empty",
        "run": lambda: solution([], []),
        "expected": [],
    },
    {
        "description": "Equal lengths: [1,2,3] and [4,5,6]",
        "run": lambda: solution([1, 2, 3], [4, 5, 6]),
        "expected": [1, 4, 2, 5, 3, 6],
    },
]
