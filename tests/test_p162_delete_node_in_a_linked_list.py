from problems.p162_delete_node_in_a_linked_list import solution, list_to_linked, linked_to_list, find_node

def _run_delete(vals, target):
    head = list_to_linked(vals)
    node = find_node(head, target)
    solution(node)
    return linked_to_list(head)

TEST_CASES = [
    {
        "description": "Delete node 5 from [4,5,1,9]",
        "run": lambda: _run_delete([4, 5, 1, 9], 5),
        "expected": [4, 1, 9],
    },
    {
        "description": "Delete node 1 from [4,5,1,9]",
        "run": lambda: _run_delete([4, 5, 1, 9], 1),
        "expected": [4, 5, 9],
    },
    {
        "description": "Delete first node from [1,2]",
        "run": lambda: _run_delete([1, 2], 1),
        "expected": [2],
    },
    {
        "description": "Delete middle of three",
        "run": lambda: _run_delete([1, 2, 3], 2),
        "expected": [1, 3],
    },
]
