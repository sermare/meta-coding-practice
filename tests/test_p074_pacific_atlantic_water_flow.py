from problems.p074_pacific_atlantic_water_flow import solution

TEST_CASES = [
    {
        "description": "5x5 island",
        "run": lambda: sorted(solution([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])),
        "expected": sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    },
    {
        "description": "Single cell: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": [[0, 0]],
    },
    {
        "description": "Flat grid: [[1,1],[1,1]]",
        "run": lambda: sorted(solution([[1, 1], [1, 1]])),
        "expected": sorted([[0, 0], [0, 1], [1, 0], [1, 1]]),
    },
    {
        "description": "Descending grid: [[3,2],[2,1]]",
        "run": lambda: sorted(solution([[3, 2], [2, 1]])),
        "expected": sorted([[0, 0], [0, 1], [1, 0], [1, 1]]),
    },
]
