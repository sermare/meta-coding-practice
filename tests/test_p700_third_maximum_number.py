from problems.p700_third_maximum_number import solution

TEST_CASES = [
    {
        "description": "Three distinct: [3,2,1]",
        "run": lambda: solution([3, 2, 1]),
        "expected": 1,
    },
    {
        "description": "Less than three distinct: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": 2,
    },
    {
        "description": "Duplicates: [2,2,3,1]",
        "run": lambda: solution([2, 2, 3, 1]),
        "expected": 1,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Negative numbers: [-1,-2,-3]",
        "run": lambda: solution([-1, -2, -3]),
        "expected": -3,
    },
]
