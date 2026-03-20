from problems.p280_maximum_xor_of_two_numbers import solution

TEST_CASES = [
    {
        "description": "[3,10,5,25,2,8] -> 28",
        "run": lambda: solution([3, 10, 5, 25, 2, 8]),
        "expected": 28,
    },
    {
        "description": "[14,70,53,83,49,91,36,80,92,51,66,70] -> 127",
        "run": lambda: solution([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]),
        "expected": 127,
    },
    {
        "description": "[0] -> 0",
        "run": lambda: solution([0]),
        "expected": 0,
    },
    {
        "description": "[1,2] -> 3",
        "run": lambda: solution([1, 2]),
        "expected": 3,
    },
    {
        "description": "[8,10,2] -> 10",
        "run": lambda: solution([8, 10, 2]),
        "expected": 10,
    },
]
