from problems.p268_flatten_nested_list_iterator import solution

TEST_CASES = [
    {
        "description": "[[1,1],2,[1,1]] -> [1,1,2,1,1]",
        "run": lambda: solution([[1, 1], 2, [1, 1]]),
        "expected": [1, 1, 2, 1, 1],
    },
    {
        "description": "[1,[4,[6]]] -> [1,4,6]",
        "run": lambda: solution([1, [4, [6]]]),
        "expected": [1, 4, 6],
    },
    {
        "description": "[] -> []",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "[[]] -> []",
        "run": lambda: solution([[]]),
        "expected": [],
    },
    {
        "description": "[1,2,3] flat list",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 2, 3],
    },
]
