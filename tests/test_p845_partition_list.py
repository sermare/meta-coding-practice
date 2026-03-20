from problems.p845_partition_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Partition around 3: [1,4,3,2,5,2]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,4,3,2,5,2]), 3)),
        "expected": [1,2,2,4,3,5],
    },
    {
        "description": "Partition around 1: [2,1]",
        "run": lambda: linked_to_list(solution(list_to_linked([2,1]), 1)),
        "expected": [2,1],
    },
    {
        "description": "All less: [1,2,3] x=5",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]), 5)),
        "expected": [1,2,3],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]), 1)),
        "expected": [],
    },
]
