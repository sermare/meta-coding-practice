from problems.p177_populating_next_right_pointers import solution, build_tree, collect_next_pointers

TEST_CASES = [
    {
        "description": "Perfect tree [1,2,3,4,5,6,7]",
        "run": lambda: collect_next_pointers(solution(build_tree([1,2,3,4,5,6,7]))),
        "expected": [[1,None],[2,3,None],[4,5,6,7,None]],
    },
    {
        "description": "Single node",
        "run": lambda: collect_next_pointers(solution(build_tree([1]))),
        "expected": [[1, None]],
    },
    {
        "description": "Empty tree",
        "run": lambda: collect_next_pointers(solution(build_tree([]))),
        "expected": [],
    },
    {
        "description": "Two-level tree [1,2,3]",
        "run": lambda: collect_next_pointers(solution(build_tree([1,2,3]))),
        "expected": [[1,None],[2,3,None]],
    },
]
