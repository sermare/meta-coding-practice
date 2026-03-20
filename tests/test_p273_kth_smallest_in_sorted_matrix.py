from problems.p273_kth_smallest_in_sorted_matrix import solution

TEST_CASES = [
    {
        "description": "[[1,5,9],[10,11,13],[12,13,15]] k=8 -> 13",
        "run": lambda: solution([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
        "expected": 13,
    },
    {
        "description": "[[-5]] k=1 -> -5",
        "run": lambda: solution([[-5]], 1),
        "expected": -5,
    },
    {
        "description": "[[1,2],[1,3]] k=2 -> 1",
        "run": lambda: solution([[1, 2], [1, 3]], 2),
        "expected": 1,
    },
    {
        "description": "[[1,2],[3,4]] k=4 -> 4",
        "run": lambda: solution([[1, 2], [3, 4]], 4),
        "expected": 4,
    },
    {
        "description": "[[1,3,5],[6,7,12],[11,14,14]] k=6 -> 11",
        "run": lambda: solution([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6),
        "expected": 11,
    },
]
