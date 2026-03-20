from problems.p666_walls_and_gates import solution

INF = 2147483647

TEST_CASES = [
    {
        "description": "Standard grid with gates and walls",
        "run": lambda: solution([
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ]),
        "expected": [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    },
    {
        "description": "All walls",
        "run": lambda: solution([[-1, -1], [-1, -1]]),
        "expected": [[-1, -1], [-1, -1]],
    },
    {
        "description": "Single gate",
        "run": lambda: solution([[0]]),
        "expected": [[0]],
    },
    {
        "description": "No gates",
        "run": lambda: solution([[INF, INF], [INF, INF]]),
        "expected": [[INF, INF], [INF, INF]],
    },
]
