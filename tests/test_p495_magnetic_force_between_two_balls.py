from problems.p495_magnetic_force_between_two_balls import solution

TEST_CASES = [
    {
        "description": "[1,2,3,4,7] m=3 -> 3",
        "run": lambda: solution([1,2,3,4,7], 3),
        "expected": 3,
    },
    {
        "description": "Large gap: m=2 -> 999999999",
        "run": lambda: solution([5,4,3,2,1,1000000000], 2),
        "expected": 999999999,
    },
    {
        "description": "[1,2,3] m=2 -> 2",
        "run": lambda: solution([1,2,3], 2),
        "expected": 2,
    },
    {
        "description": "All positions: [1,2,3] m=3 -> 1",
        "run": lambda: solution([1,2,3], 3),
        "expected": 1,
    },
    {
        "description": "[1,10,20,30] m=2 -> 29",
        "run": lambda: solution([1,10,20,30], 2),
        "expected": 29,
    },
]
