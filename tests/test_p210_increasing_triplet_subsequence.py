from problems.p210_increasing_triplet_subsequence import solution

TEST_CASES = [
    {
        "description": "Increasing: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": True,
    },
    {
        "description": "Decreasing: [5,4,3,2,1]",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": False,
    },
    {
        "description": "Hidden triplet: [2,1,5,0,4,6]",
        "run": lambda: solution([2, 1, 5, 0, 4, 6]),
        "expected": True,
    },
    {
        "description": "Two elements only: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": False,
    },
    {
        "description": "All same: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": False,
    },
]
