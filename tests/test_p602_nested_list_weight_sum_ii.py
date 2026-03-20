from problems.p602_nested_list_weight_sum_ii import solution

TEST_CASES = [
    {
        "description": "Basic nested: [[1,1],2,[1,1]]",
        "run": lambda: solution([[1, 1], 2, [1, 1]]),
        "expected": 8,
    },
    {
        "description": "Deeper nesting: [1,[4,[6]]]",
        "run": lambda: solution([1, [4, [6]]]),
        "expected": 17,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "All at depth 1: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 6,
    },
    {
        "description": "Deeply nested: [[[[1]]]]",
        "run": lambda: solution([[[[1]]]]),
        "expected": 1,
    },
]
