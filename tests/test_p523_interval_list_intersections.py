from problems.p523_interval_list_intersections import solution

TEST_CASES = [
    {
        "description": "Basic intersections",
        "run": lambda: solution([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),
        "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
    },
    {
        "description": "No intersection",
        "run": lambda: solution([[1,2]], [[3,4]]),
        "expected": [],
    },
    {
        "description": "Complete overlap",
        "run": lambda: solution([[1,5]], [[1,5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "Empty first list",
        "run": lambda: solution([], [[1,5]]),
        "expected": [],
    },
    {
        "description": "One contains other",
        "run": lambda: solution([[1,10]], [[2,3],[5,7]]),
        "expected": [[2, 3], [5, 7]],
    },
]
