from problems.p567_vertical_order_traversal_of_a_binary_tree import solution

TEST_CASES = [
    {
        "description": "Basic tree: [3,9,20,None,None,15,7]",
        "run": lambda: solution([3, 9, 20, None, None, 15, 7]),
        "expected": [[9], [3, 15], [20], [7]],
    },
    {
        "description": "Full tree: [1,2,3,4,5,6,7]",
        "run": lambda: solution([1, 2, 3, 4, 5, 6, 7]),
        "expected": [[4], [2], [1, 5, 6], [3], [7]],
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
]
