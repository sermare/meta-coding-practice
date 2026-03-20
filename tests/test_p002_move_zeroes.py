from problems.p002_move_zeroes import solution

TEST_CASES = [
    {
        "description": "Mixed zeroes and non-zeroes: [0,1,0,3,12]",
        "run": lambda: solution([0, 1, 0, 3, 12]),
        "expected": [1, 3, 12, 0, 0],
    },
    {
        "description": "Single zero: [0]",
        "run": lambda: solution([0]),
        "expected": [0],
    },
    {
        "description": "Single non-zero: [1]",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Leading zeroes: [0,0,0,1]",
        "run": lambda: solution([0, 0, 0, 1]),
        "expected": [1, 0, 0, 0],
    },
    {
        "description": "No zeroes: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 2, 3],
    },
]
