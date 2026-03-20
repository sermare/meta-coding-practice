from problems.p792_divide_array_into_equal_pairs import solution

TEST_CASES = [
    {
        "description": "Can pair: [3,2,3,2,2,2]",
        "run": lambda: solution([3,2,3,2,2,2]),
        "expected": True,
    },
    {
        "description": "Cannot pair: [1,2,3,4]",
        "run": lambda: solution([1,2,3,4]),
        "expected": False,
    },
    {
        "description": "All same: [1,1,1,1]",
        "run": lambda: solution([1,1,1,1]),
        "expected": True,
    },
    {
        "description": "Single pair: [5,5]",
        "run": lambda: solution([5,5]),
        "expected": True,
    },
]
