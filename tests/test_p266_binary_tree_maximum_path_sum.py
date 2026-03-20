from problems.p266_binary_tree_maximum_path_sum import solution, build_tree

TEST_CASES = [
    {
        "description": "[-10,9,20,null,null,15,7] -> 42",
        "run": lambda: solution(build_tree([-10, 9, 20, None, None, 15, 7])),
        "expected": 42,
    },
    {
        "description": "[1,2,3] -> 6",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": 6,
    },
    {
        "description": "[-3] -> -3",
        "run": lambda: solution(build_tree([-3])),
        "expected": -3,
    },
    {
        "description": "[2,-1] -> 2",
        "run": lambda: solution(build_tree([2, -1])),
        "expected": 2,
    },
    {
        "description": "[5,4,8,11,None,13,4,7,2,None,None,None,1] -> 48",
        "run": lambda: solution(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])),
        "expected": 48,
    },
]
