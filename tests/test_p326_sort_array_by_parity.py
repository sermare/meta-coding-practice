from problems.p326_sort_array_by_parity import solution

TEST_CASES = [
    {
        "description": "Basic: [3,1,2,4]",
        "run": lambda: (lambda r: all(r[i] % 2 == 0 for i in range(2)) and all(r[i] % 2 == 1 for i in range(2, 4)) and sorted(r) == [1, 2, 3, 4])(solution([3, 1, 2, 4])),
        "expected": True,
    },
    {
        "description": "All even: [2,4,6]",
        "run": lambda: sorted(solution([2, 4, 6])),
        "expected": [2, 4, 6],
    },
    {
        "description": "All odd: [1,3,5]",
        "run": lambda: sorted(solution([1, 3, 5])),
        "expected": [1, 3, 5],
    },
    {
        "description": "Single element: [0]",
        "run": lambda: solution([0]),
        "expected": [0],
    },
]
