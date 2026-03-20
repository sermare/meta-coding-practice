from problems.p537_missing_number import solution

TEST_CASES = [
    {
        "description": "Missing 2",
        "run": lambda: solution([3,0,1]),
        "expected": 2,
    },
    {
        "description": "Missing 2 again",
        "run": lambda: solution([0,1]),
        "expected": 2,
    },
    {
        "description": "Missing 8",
        "run": lambda: solution([9,6,4,2,3,5,7,0,1]),
        "expected": 8,
    },
    {
        "description": "Missing 0",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "Missing 1",
        "run": lambda: solution([0]),
        "expected": 1,
    },
]
