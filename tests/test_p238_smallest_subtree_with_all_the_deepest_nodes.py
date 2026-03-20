from problems.p238_smallest_subtree_with_all_the_deepest_nodes import solution, build_tree

TEST_CASES = [
    {
        "description": "Standard tree: [3,5,1,6,2,0,8,None,None,7,4]",
        "run": lambda: solution(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])),
        "expected": 2,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "One deepest on each side: [0,1,3,None,2]",
        "run": lambda: solution(build_tree([0, 1, 3, None, 2])),
        "expected": 2,
    },
    {
        "description": "Balanced: [1,2,3]",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": 1,
    },
]
