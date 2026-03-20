from problems.p464_copy_list_with_random_pointer import solution, build_random_list, serialize_random_list

TEST_CASES = [
    {
        "description": "Five nodes with randoms",
        "run": lambda: serialize_random_list(solution(build_random_list([[7,None],[13,0],[11,4],[10,2],[1,0]]))),
        "expected": [[7,None],[13,0],[11,4],[10,2],[1,0]],
    },
    {
        "description": "Two nodes pointing to each other",
        "run": lambda: serialize_random_list(solution(build_random_list([[1,1],[2,1]]))),
        "expected": [[1,1],[2,1]],
    },
    {
        "description": "Single node no random",
        "run": lambda: serialize_random_list(solution(build_random_list([[1,None]]))),
        "expected": [[1,None]],
    },
    {
        "description": "Empty list",
        "run": lambda: serialize_random_list(solution(build_random_list([]))),
        "expected": [],
    },
    {
        "description": "Self-referencing random",
        "run": lambda: serialize_random_list(solution(build_random_list([[3,0],[4,0]]))),
        "expected": [[3,0],[4,0]],
    },
]
