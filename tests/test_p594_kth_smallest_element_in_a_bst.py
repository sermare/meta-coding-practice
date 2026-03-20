from problems.p594_kth_smallest_element_in_a_bst import solution

TEST_CASES = [
    {
        "description": "k=1: [3,1,4,None,2] -> 1",
        "run": lambda: solution([3, 1, 4, None, 2], 1),
        "expected": 1,
    },
    {
        "description": "k=3: [5,3,6,2,4,None,None,1] -> 3",
        "run": lambda: solution([5, 3, 6, 2, 4, None, None, 1], 3),
        "expected": 3,
    },
    {
        "description": "Single node k=1",
        "run": lambda: solution([1], 1),
        "expected": 1,
    },
    {
        "description": "k=2: [2,1,3] -> 2",
        "run": lambda: solution([2, 1, 3], 2),
        "expected": 2,
    },
]
