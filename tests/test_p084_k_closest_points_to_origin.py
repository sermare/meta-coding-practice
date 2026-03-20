from problems.p084_k_closest_points_to_origin import solution

TEST_CASES = [
    {
        "description": "Basic: [[1,3],[-2,2]] k=1",
        "run": lambda: solution([[1, 3], [-2, 2]], 1),
        "expected": [[-2, 2]],
    },
    {
        "description": "k=2: [[3,3],[5,-1],[-2,4]]",
        "run": lambda: sorted(solution([[3, 3], [5, -1], [-2, 4]], 2)),
        "expected": sorted([[3, 3], [-2, 4]]),
    },
    {
        "description": "Single point: [[0,1]] k=1",
        "run": lambda: solution([[0, 1]], 1),
        "expected": [[0, 1]],
    },
    {
        "description": "Origin point: [[0,0],[1,1]] k=1",
        "run": lambda: solution([[0, 0], [1, 1]], 1),
        "expected": [[0, 0]],
    },
]
