from problems.p480_next_greater_element_ii import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,1] -> [2,-1,2]",
        "run": lambda: solution([1,2,1]),
        "expected": [2,-1,2],
    },
    {
        "description": "Increasing: [1,2,3,4,3]",
        "run": lambda: solution([1,2,3,4,3]),
        "expected": [2,3,4,-1,4],
    },
    {
        "description": "All same: [5,5,5]",
        "run": lambda: solution([5,5,5]),
        "expected": [-1,-1,-1],
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": [-1],
    },
    {
        "description": "Decreasing: [3,2,1]",
        "run": lambda: solution([3,2,1]),
        "expected": [-1,3,3],
    },
]
