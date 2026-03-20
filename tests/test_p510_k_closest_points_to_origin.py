from problems.p510_k_closest_points_to_origin import solution

TEST_CASES = [
    {
        "description": "Basic case k=1",
        "run": lambda: solution([[1,3],[-2,2]], 1),
        "expected": [[-2, 2]],
    },
    {
        "description": "k=2",
        "run": lambda: sorted(solution([[3,3],[5,-1],[-2,4]], 2)),
        "expected": sorted([[3,3],[-2,4]]),
    },
    {
        "description": "Origin point",
        "run": lambda: solution([[0,0],[1,1]], 1),
        "expected": [[0, 0]],
    },
    {
        "description": "Single point",
        "run": lambda: solution([[1,1]], 1),
        "expected": [[1, 1]],
    },
    {
        "description": "All points",
        "run": lambda: sorted(solution([[1,0],[0,1]], 2)),
        "expected": sorted([[1,0],[0,1]]),
    },
]
