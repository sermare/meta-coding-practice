from problems.p339_kids_with_the_greatest_number_of_candies import solution

TEST_CASES = [
    {
        "description": "Basic: [2,3,5,1,3] extra=3",
        "run": lambda: solution([2, 3, 5, 1, 3], 3),
        "expected": [True, True, True, False, True],
    },
    {
        "description": "All can be greatest: [4,2,1,1,2] extra=1",
        "run": lambda: solution([4, 2, 1, 1, 2], 1),
        "expected": [True, False, False, False, False],
    },
    {
        "description": "Large extra: [1,1,1] extra=10",
        "run": lambda: solution([1, 1, 1], 10),
        "expected": [True, True, True],
    },
    {
        "description": "Single kid: [5] extra=0",
        "run": lambda: solution([5], 0),
        "expected": [True],
    },
]
