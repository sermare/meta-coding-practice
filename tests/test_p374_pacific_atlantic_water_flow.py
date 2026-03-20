from problems.p374_pacific_atlantic_water_flow import solution


TEST_CASES = [
    {
        "description": "Standard 5x5 grid",
        "run": lambda: sorted(solution([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])),
        "expected": [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
    },
    {
        "description": "Single cell",
        "run": lambda: solution([[1]]),
        "expected": [[0, 0]],
    },
    {
        "description": "1x2 grid",
        "run": lambda: sorted(solution([[1, 1]])),
        "expected": [[0, 0], [0, 1]],
    },
    {
        "description": "All same height",
        "run": lambda: sorted(solution([[1, 1], [1, 1]])),
        "expected": [[0, 0], [0, 1], [1, 0], [1, 1]],
    },
]
