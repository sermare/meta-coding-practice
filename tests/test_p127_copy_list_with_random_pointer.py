from problems.p127_copy_list_with_random_pointer import solution, build_list, list_to_pairs

TEST_CASES = [
    {
        "description": "Standard list with random pointers",
        "run": lambda: list_to_pairs(solution(build_list([[7,None],[13,0],[11,4],[10,2],[1,0]]))),
        "expected": [[7,None],[13,0],[11,4],[10,2],[1,0]],
    },
    {
        "description": "Two nodes pointing to each other",
        "run": lambda: list_to_pairs(solution(build_list([[1,1],[2,0]]))),
        "expected": [[1,1],[2,0]],
    },
    {
        "description": "All random pointers null",
        "run": lambda: list_to_pairs(solution(build_list([[1,None],[2,None],[3,None]]))),
        "expected": [[1,None],[2,None],[3,None]],
    },
    {
        "description": "Single node with self random",
        "run": lambda: list_to_pairs(solution(build_list([[5,0]]))),
        "expected": [[5,0]],
    },
]
