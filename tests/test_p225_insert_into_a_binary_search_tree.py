from problems.p225_insert_into_a_binary_search_tree import solution, build_tree, inorder

TEST_CASES = [
    {
        "description": "Insert 5 into [4,2,7,1,3]",
        "run": lambda: inorder(solution(build_tree([4, 2, 7, 1, 3]), 5)),
        "expected": [1, 2, 3, 4, 5, 7],
    },
    {
        "description": "Insert into empty tree",
        "run": lambda: inorder(solution(build_tree([]), 1)),
        "expected": [1],
    },
    {
        "description": "Insert smaller value",
        "run": lambda: inorder(solution(build_tree([4, 2, 7]), 1)),
        "expected": [1, 2, 4, 7],
    },
    {
        "description": "Insert larger value",
        "run": lambda: inorder(solution(build_tree([4, 2, 7]), 10)),
        "expected": [2, 4, 7, 10],
    },
]
