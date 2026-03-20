from problems.p303_longest_consecutive_sequence import solution

TEST_CASES = [
    {
        "description": "Basic case: [100,4,200,1,3,2]",
        "run": lambda: solution([100, 4, 200, 1, 3, 2]),
        "expected": 4,
    },
    {
        "description": "Longer sequence: [0,3,7,2,5,8,4,6,0,1]",
        "run": lambda: solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        "expected": 9,
    },
    {
        "description": "Empty array",
        "run": lambda: solution([]),
        "expected": 0,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "No consecutive",
        "run": lambda: solution([10, 20, 30]),
        "expected": 1,
    },
]
