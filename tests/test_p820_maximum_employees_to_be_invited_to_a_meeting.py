from problems.p820_maximum_employees_to_be_invited_to_a_meeting import solution

TEST_CASES = [
    {
        "description": "Basic: [2,2,1,2]",
        "run": lambda: solution([2, 2, 1, 2]),
        "expected": 3,
    },
    {
        "description": "Cycle of 3: [1,2,0]",
        "run": lambda: solution([1, 2, 0]),
        "expected": 3,
    },
    {
        "description": "Mutual pairs: [3,0,1,4,1]",
        "run": lambda: solution([3, 0, 1, 4, 1]),
        "expected": 4,
    },
    {
        "description": "Self loop: [0]",
        "run": lambda: solution([0]),
        "expected": 1,
    },
]
