from problems.p638_house_robber_ii import solution

TEST_CASES = [
    {
        "description": "Circular: [2,3,2]",
        "run": lambda: solution([2, 3, 2]),
        "expected": 3,
    },
    {
        "description": "Circular: [1,2,3,1]",
        "run": lambda: solution([1, 2, 3, 1]),
        "expected": 4,
    },
    {
        "description": "Three houses: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Single house: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Two houses: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": 2,
    },
]
