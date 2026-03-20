from problems.p454_reorder_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Even length: [1,2,3,4] -> [1,4,2,3]",
        "run": lambda: (lambda h: (solution(h), linked_to_list(h)))(list_to_linked([1,2,3,4]))[1],
        "expected": [1,4,2,3],
    },
    {
        "description": "Odd length: [1,2,3,4,5] -> [1,5,2,4,3]",
        "run": lambda: (lambda h: (solution(h), linked_to_list(h)))(list_to_linked([1,2,3,4,5]))[1],
        "expected": [1,5,2,4,3],
    },
    {
        "description": "Single node: [1] -> [1]",
        "run": lambda: (lambda h: (solution(h), linked_to_list(h)))(list_to_linked([1]))[1],
        "expected": [1],
    },
    {
        "description": "Two nodes: [1,2] -> [1,2]",
        "run": lambda: (lambda h: (solution(h), linked_to_list(h)))(list_to_linked([1,2]))[1],
        "expected": [1,2],
    },
    {
        "description": "Three nodes: [1,2,3] -> [1,3,2]",
        "run": lambda: (lambda h: (solution(h), linked_to_list(h)))(list_to_linked([1,2,3]))[1],
        "expected": [1,3,2],
    },
]
