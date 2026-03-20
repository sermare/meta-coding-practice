from problems.p769_count_nodes_equal_to_average_of_subtree import solution

TEST_CASES = [
    {
        "description": "Basic tree: [4,8,5,0,1,None,6]",
        "run": lambda: solution([4,8,5,0,1,None,6]),
        "expected": 5,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All same values: [5,5,5]",
        "run": lambda: solution([5,5,5]),
        "expected": 3,
    },
    {
        "description": "Two nodes: [2,1]",
        "run": lambda: solution([2,1]),
        "expected": 1,
    },
]
