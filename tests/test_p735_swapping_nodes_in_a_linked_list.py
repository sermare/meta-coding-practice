from problems.p735_swapping_nodes_in_a_linked_list import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,2,3,4,5], k=2",
        "run": lambda: solution([1, 2, 3, 4, 5], 2),
        "expected": [1, 4, 3, 2, 5],
    },
    {
        "description": "Swap first and last: [1,2,3], k=1",
        "run": lambda: solution([1, 2, 3], 1),
        "expected": [3, 2, 1],
    },
    {
        "description": "Single element: [1], k=1",
        "run": lambda: solution([1], 1),
        "expected": [1],
    },
    {
        "description": "Same position: [1,2,3], k=2",
        "run": lambda: solution([1, 2, 3], 2),
        "expected": [1, 2, 3],
    },
]
