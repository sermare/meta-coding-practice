from problems.p218_matchsticks_to_square import solution

TEST_CASES = [
    {
        "description": "Can form square: [1,1,2,2,2]",
        "run": lambda: solution([1, 1, 2, 2, 2]),
        "expected": True,
    },
    {
        "description": "Cannot form square: [3,3,3,3,4]",
        "run": lambda: solution([3, 3, 3, 3, 4]),
        "expected": False,
    },
    {
        "description": "All equal: [2,2,2,2]",
        "run": lambda: solution([2, 2, 2, 2]),
        "expected": True,
    },
    {
        "description": "Single stick: [4]",
        "run": lambda: solution([4]),
        "expected": False,
    },
    {
        "description": "Larger: [5,5,5,5,4,4,4,4,3,3,3,3]",
        "run": lambda: solution([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]),
        "expected": True,
    },
]
