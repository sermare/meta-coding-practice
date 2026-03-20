from problems.p496_single_element_in_a_sorted_array import solution

TEST_CASES = [
    {
        "description": "Middle: [1,1,2,3,3,4,4,8,8] -> 2",
        "run": lambda: solution([1,1,2,3,3,4,4,8,8]),
        "expected": 2,
    },
    {
        "description": "Near end: [3,3,7,7,10,11,11] -> 10",
        "run": lambda: solution([3,3,7,7,10,11,11]),
        "expected": 10,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "At start: [2,3,3]",
        "run": lambda: solution([2,3,3]),
        "expected": 2,
    },
    {
        "description": "At end: [1,1,2]",
        "run": lambda: solution([1,1,2]),
        "expected": 2,
    },
]
