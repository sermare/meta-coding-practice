from problems.p744_finding_3-digit_even_numbers import solution

TEST_CASES = [
    {
        "description": "Basic case: [2,1,3,0]",
        "run": lambda: solution([2, 1, 3, 0]),
        "expected": [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
    },
    {
        "description": "All same: [2,2,2]",
        "run": lambda: solution([2, 2, 2]),
        "expected": [222],
    },
    {
        "description": "Only odd digits: [1,3,5]",
        "run": lambda: solution([1, 3, 5]),
        "expected": [],
    },
    {
        "description": "With zeros: [0,0,0]",
        "run": lambda: solution([0, 0, 0]),
        "expected": [],
    },
]
