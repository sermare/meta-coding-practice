from problems.p414_target_sum import solution

TEST_CASES = [
    {
        "description": "Basic: nums=[1,1,1,1,1] target=3",
        "run": lambda: solution([1, 1, 1, 1, 1], 3),
        "expected": 5,
    },
    {
        "description": "Single element match: nums=[1] target=1",
        "run": lambda: solution([1], 1),
        "expected": 1,
    },
    {
        "description": "No way: nums=[1] target=2",
        "run": lambda: solution([1], 2),
        "expected": 0,
    },
    {
        "description": "All zeros: nums=[0,0,0] target=0",
        "run": lambda: solution([0, 0, 0], 0),
        "expected": 8,
    },
    {
        "description": "Two elements: nums=[1,2] target=1",
        "run": lambda: solution([1, 2], 1),
        "expected": 1,
    },
]
