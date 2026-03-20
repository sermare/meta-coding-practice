from problems.p412_longest_increasing_subsequence import solution

TEST_CASES = [
    {
        "description": "Basic: [10,9,2,5,3,7,101,18]",
        "run": lambda: solution([10, 9, 2, 5, 3, 7, 101, 18]),
        "expected": 4,
    },
    {
        "description": "Already sorted: [0,1,0,3,2,3]",
        "run": lambda: solution([0, 1, 0, 3, 2, 3]),
        "expected": 4,
    },
    {
        "description": "All same: [7,7,7,7,7]",
        "run": lambda: solution([7, 7, 7, 7, 7]),
        "expected": 1,
    },
    {
        "description": "Single element: [10]",
        "run": lambda: solution([10]),
        "expected": 1,
    },
    {
        "description": "Decreasing: [5,4,3,2,1]",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": 1,
    },
]
