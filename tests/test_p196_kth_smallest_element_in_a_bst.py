from problems.p196_kth_smallest_element_in_a_bst import solution, build_tree

TEST_CASES = [
    {
        "description": "k=1 in [3,1,4,None,2]",
        "run": lambda: solution(build_tree([3, 1, 4, None, 2]), 1),
        "expected": 1,
    },
    {
        "description": "k=3 in [5,3,6,2,4,None,None,1]",
        "run": lambda: solution(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3),
        "expected": 3,
    },
    {
        "description": "Single node k=1",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": 1,
    },
    {
        "description": "k=2 in [2,1,3]",
        "run": lambda: solution(build_tree([2, 1, 3]), 2),
        "expected": 2,
    },
]
