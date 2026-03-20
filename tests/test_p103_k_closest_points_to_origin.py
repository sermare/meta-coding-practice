from problems.p103_k_closest_points_to_origin import solution

TEST_CASES = [
    {
        "description": "Single closest point",
        "run": lambda: sorted(solution([[1, 3], [-2, 2]], 1)),
        "expected": [[-2, 2]],
    },
    {
        "description": "Two closest of three",
        "run": lambda: sorted(solution([[3, 3], [5, -1], [-2, 4]], 2)),
        "expected": [[-2, 4], [3, 3]],
    },
    {
        "description": "All points returned",
        "run": lambda: sorted(solution([[0, 1], [1, 0]], 2)),
        "expected": [[0, 1], [1, 0]],
    },
    {
        "description": "Origin point present",
        "run": lambda: sorted(solution([[0, 0], [1, 1], [2, 2]], 1)),
        "expected": [[0, 0]],
    },
    {
        "description": "Negative coordinates",
        "run": lambda: sorted(solution([[-5, 4], [1, -1], [3, 2], [-1, 0]], 2)),
        "expected": [[-1, 0], [1, -1]],
    },
]
