from problems.p830_maximum_beauty_of_an_array_after_applying_operation import solution

TEST_CASES = [
    {
        "description": "Basic: [4,6,1,2] k=2",
        "run": lambda: solution([4,6,1,2], 2),
        "expected": 3,
    },
    {
        "description": "All same: [1,1,1] k=0",
        "run": lambda: solution([1,1,1], 0),
        "expected": 3,
    },
    {
        "description": "Single element: [5] k=10",
        "run": lambda: solution([5], 10),
        "expected": 1,
    },
    {
        "description": "Far apart: [1,100] k=2",
        "run": lambda: solution([1,100], 2),
        "expected": 1,
    },
]
