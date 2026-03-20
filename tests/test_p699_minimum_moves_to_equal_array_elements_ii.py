from problems.p699_minimum_moves_to_equal_array_elements_ii import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 2,
    },
    {
        "description": "Already equal: [5,5,5]",
        "run": lambda: solution([5, 5, 5]),
        "expected": 0,
    },
    {
        "description": "Two elements: [1,10]",
        "run": lambda: solution([1, 10]),
        "expected": 9,
    },
    {
        "description": "Larger: [1,0,0,8,6]",
        "run": lambda: solution([1, 0, 0, 8, 6]),
        "expected": 14,
    },
]
