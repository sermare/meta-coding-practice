from problems.p205_house_robber_ii import solution

TEST_CASES = [
    {
        "description": "Three houses: [2,3,2]",
        "run": lambda: solution([2, 3, 2]),
        "expected": 3,
    },
    {
        "description": "Four houses: [1,2,3,1]",
        "run": lambda: solution([1, 2, 3, 1]),
        "expected": 4,
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
    {
        "description": "Larger: [1,2,3,4,5,1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
        "expected": 16,
    },
]
