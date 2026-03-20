from problems.p048_longest_increasing_subsequence import solution

TEST_CASES = [
    {
        "description": "[10,9,2,5,3,7,101,18] -> 4",
        "run": lambda: solution([10, 9, 2, 5, 3, 7, 101, 18]),
        "expected": 4,
    },
    {
        "description": "[0,1,0,3,2,3] -> 4",
        "run": lambda: solution([0, 1, 0, 3, 2, 3]),
        "expected": 4,
    },
    {
        "description": "All same values -> 1",
        "run": lambda: solution([7, 7, 7, 7, 7]),
        "expected": 1,
    },
    {
        "description": "Single element -> 1",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "[3,5,6,2,5,4,19,5,6,7,12] -> 6",
        "run": lambda: solution([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]),
        "expected": 6,
    },
]
