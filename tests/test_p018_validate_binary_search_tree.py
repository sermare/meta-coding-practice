from problems.p018_validate_binary_search_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Valid BST: [2,1,3]",
        "run": lambda: solution(build_tree([2, 1, 3])),
        "expected": True,
    },
    {
        "description": "Invalid BST: [5,1,4,None,None,3,6]",
        "run": lambda: solution(build_tree([5, 1, 4, None, None, 3, 6])),
        "expected": False,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": True,
    },
    {
        "description": "Empty tree: []",
        "run": lambda: solution(build_tree([])),
        "expected": True,
    },
    {
        "description": "Invalid BST with deeper violation: [5,4,6,None,None,3,7]",
        "run": lambda: solution(build_tree([5, 4, 6, None, None, 3, 7])),
        "expected": False,
    },
]
