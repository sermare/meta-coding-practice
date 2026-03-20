from problems.p689_robot_room_cleaner import solution

TEST_CASES = [
    {
        "description": "3x3 room with wall in center",
        "run": lambda: sorted(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 0, 0)),
        "expected": sorted([[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]),
    },
    {
        "description": "Fully open 2x2 room",
        "run": lambda: sorted(solution([[1, 1], [1, 1]], 0, 0)),
        "expected": sorted([[0,0],[0,1],[1,0],[1,1]]),
    },
    {
        "description": "Single cell",
        "run": lambda: solution([[1]], 0, 0),
        "expected": [[0, 0]],
    },
    {
        "description": "Blocked start",
        "run": lambda: sorted(solution([[1, 0], [0, 1]], 0, 0)),
        "expected": [[0, 0]],
    },
]
