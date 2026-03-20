from problems.p337_shuffle_the_array import solution

TEST_CASES = [
    {
        "description": "Basic: [2,5,1,3,4,7] n=3",
        "run": lambda: solution([2, 5, 1, 3, 4, 7], 3),
        "expected": [2, 3, 5, 4, 1, 7],
    },
    {
        "description": "Simple: [1,1,2,2] n=2",
        "run": lambda: solution([1, 1, 2, 2], 2),
        "expected": [1, 2, 1, 2],
    },
    {
        "description": "Minimal: [1,2] n=1",
        "run": lambda: solution([1, 2], 1),
        "expected": [1, 2],
    },
    {
        "description": "Four pairs: [1,2,3,4,5,6,7,8] n=4",
        "run": lambda: solution([1, 2, 3, 4, 5, 6, 7, 8], 4),
        "expected": [1, 5, 2, 6, 3, 7, 4, 8],
    },
]
