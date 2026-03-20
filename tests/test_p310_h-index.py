from problems.p310_h-index import solution

TEST_CASES = [
    {
        "description": "Basic: [3,0,6,1,5] -> 3",
        "run": lambda: solution([3, 0, 6, 1, 5]),
        "expected": 3,
    },
    {
        "description": "All same: [1,1,1] -> 1",
        "run": lambda: solution([1, 1, 1]),
        "expected": 1,
    },
    {
        "description": "All high: [10,10,10] -> 3",
        "run": lambda: solution([10, 10, 10]),
        "expected": 3,
    },
    {
        "description": "Single paper: [100] -> 1",
        "run": lambda: solution([100]),
        "expected": 1,
    },
    {
        "description": "No citations: [0,0,0] -> 0",
        "run": lambda: solution([0, 0, 0]),
        "expected": 0,
    },
]
