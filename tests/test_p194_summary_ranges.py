from problems.p194_summary_ranges import solution

TEST_CASES = [
    {
        "description": "[0,1,2,4,5,7]",
        "run": lambda: solution([0, 1, 2, 4, 5, 7]),
        "expected": ["0->2", "4->5", "7"],
    },
    {
        "description": "[0,2,3,4,6,8,9]",
        "run": lambda: solution([0, 2, 3, 4, 6, 8, 9]),
        "expected": ["0", "2->4", "6", "8->9"],
    },
    {
        "description": "Empty array",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Single element",
        "run": lambda: solution([5]),
        "expected": ["5"],
    },
]
