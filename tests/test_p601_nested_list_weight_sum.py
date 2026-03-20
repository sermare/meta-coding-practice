from problems.p601_nested_list_weight_sum import solution

TEST_CASES = [
    {
        "description": "Basic nested: [[1,1],2,[1,1]]",
        "run": lambda: solution([[1, 1], 2, [1, 1]]),
        "expected": 10,
    },
    {
        "description": "Deeper nesting: [1,[4,[6]]]",
        "run": lambda: solution([1, [4, [6]]]),
        "expected": 27,
    },
    {
        "description": "Single element: [0]",
        "run": lambda: solution([0]),
        "expected": 0,
    },
    {
        "description": "All at depth 1: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 6,
    },
    {
        "description": "Deeply nested: [[[[1]]]]",
        "run": lambda: solution([[[[1]]]]),
        "expected": 4,
    },
]
