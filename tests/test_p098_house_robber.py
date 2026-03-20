from problems.p098_house_robber import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,1] -> 4",
        "run": lambda: solution([1, 2, 3, 1]),
        "expected": 4,
    },
    {
        "description": "Larger: [2,7,9,3,1] -> 12",
        "run": lambda: solution([2, 7, 9, 3, 1]),
        "expected": 12,
    },
    {
        "description": "Single house: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Two houses: [2,3]",
        "run": lambda: solution([2, 3]),
        "expected": 3,
    },
    {
        "description": "All same: [3,3,3,3]",
        "run": lambda: solution([3, 3, 3, 3]),
        "expected": 6,
    },
]
