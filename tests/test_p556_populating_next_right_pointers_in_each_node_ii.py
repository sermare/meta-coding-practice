from problems.p556_populating_next_right_pointers_in_each_node_ii import solution

TEST_CASES = [
    {
        "description": "Complete-ish tree: [1,2,3,4,5,None,7]",
        "run": lambda: solution([1, 2, 3, 4, 5, None, 7]),
        "expected": {1: None, 2: 3, 3: None, 4: 5, 5: 7, 7: None},
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": {1: None},
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": {},
    },
    {
        "description": "Left-skewed: [1,2,None,3]",
        "run": lambda: solution([1, 2, None, 3]),
        "expected": {1: None, 2: None, 3: None},
    },
]
