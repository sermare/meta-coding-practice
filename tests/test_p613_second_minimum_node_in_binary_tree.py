from problems.p613_second_minimum_node_in_binary_tree import solution

TEST_CASES = [
    {
        "description": "Basic tree: [2,2,5,null,null,5,7]",
        "run": lambda: solution([2, 2, 5, None, None, 5, 7]),
        "expected": 5,
    },
    {
        "description": "All same values: [2,2,2]",
        "run": lambda: solution([2, 2, 2]),
        "expected": -1,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": -1,
    },
    {
        "description": "Two distinct values: [1,1,3]",
        "run": lambda: solution([1, 1, 3]),
        "expected": 3,
    },
]
