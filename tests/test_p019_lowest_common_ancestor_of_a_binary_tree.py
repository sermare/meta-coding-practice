from problems.p019_lowest_common_ancestor_of_a_binary_tree import (
    solution,
    build_tree,
    find_node,
)


def _run_lca(values, p_val, q_val):
    root = build_tree(values)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    result = solution(root, p, q)
    return result.val if result else None


TEST_CASES = [
    {
        "description": "LCA of 5 and 1 in [3,5,1,6,2,0,8,None,None,7,4] is 3",
        "run": lambda: _run_lca(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1
        ),
        "expected": 3,
    },
    {
        "description": "LCA of 5 and 4 in [3,5,1,6,2,0,8,None,None,7,4] is 5",
        "run": lambda: _run_lca(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4
        ),
        "expected": 5,
    },
    {
        "description": "LCA of 1 and 2 in [1,2] is 1",
        "run": lambda: _run_lca([1, 2], 1, 2),
        "expected": 1,
    },
]
