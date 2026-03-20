from problems.p239_shortest_bridge import solution

TEST_CASES = [
    {
        "description": "Diagonal: [[0,1],[1,0]]",
        "run": lambda: solution([[0, 1], [1, 0]]),
        "expected": 1,
    },
    {
        "description": "Corners: [[0,1,0],[0,0,0],[0,0,1]]",
        "run": lambda: solution([[0, 1, 0], [0, 0, 0], [0, 0, 1]]),
        "expected": 2,
    },
    {
        "description": "Adjacent rows: [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]",
        "run": lambda: solution([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]),
        "expected": 1,
    },
    {
        "description": "Far apart: [[1,0,0,0,1]]",
        "run": lambda: solution([[1, 0, 0, 0, 1]]),
        "expected": 3,
    },
]
