from problems.p554_flatten_nested_list_iterator import solution

TEST_CASES = [
    {
        "description": "Nested lists: [[1,1],2,[1,1]]",
        "run": lambda: solution([[1, 1], 2, [1, 1]]),
        "expected": [1, 1, 2, 1, 1],
    },
    {
        "description": "Deep nesting: [1,[4,[6]]]",
        "run": lambda: solution([1, [4, [6]]]),
        "expected": [1, 4, 6],
    },
    {
        "description": "Flat list: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Empty nested: [[]]",
        "run": lambda: solution([[]]),
        "expected": [],
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": [5],
    },
]
