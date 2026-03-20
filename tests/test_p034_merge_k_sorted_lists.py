from problems.p034_merge_k_sorted_lists import (
    solution, ListNode, list_to_linkedlist, linkedlist_to_list,
)

TEST_CASES = [
    {
        "description": "[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]",
        "run": lambda: linkedlist_to_list(
            solution([
                list_to_linkedlist([1, 4, 5]),
                list_to_linkedlist([1, 3, 4]),
                list_to_linkedlist([2, 6]),
            ])
        ),
        "expected": [1, 1, 2, 3, 4, 4, 5, 6],
    },
    {
        "description": "[] -> []",
        "run": lambda: linkedlist_to_list(solution([])),
        "expected": [],
    },
    {
        "description": "[[]] -> []",
        "run": lambda: linkedlist_to_list(
            solution([list_to_linkedlist([])])
        ),
        "expected": [],
    },
    {
        "description": "[[1],[2],[3]] -> [1,2,3]",
        "run": lambda: linkedlist_to_list(
            solution([
                list_to_linkedlist([1]),
                list_to_linkedlist([2]),
                list_to_linkedlist([3]),
            ])
        ),
        "expected": [1, 2, 3],
    },
    {
        "description": "[[-1,0,1],[-2,0,2]] -> [-2,-1,0,0,1,2]",
        "run": lambda: linkedlist_to_list(
            solution([
                list_to_linkedlist([-1, 0, 1]),
                list_to_linkedlist([-2, 0, 2]),
            ])
        ),
        "expected": [-2, -1, 0, 0, 1, 2],
    },
]
