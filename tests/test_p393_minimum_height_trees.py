from problems.p393_minimum_height_trees import solution


TEST_CASES = [
    {
        "description": "Star graph: center is root",
        "run": lambda: solution(4, [[1, 0], [1, 2], [1, 3]]),
        "expected": [1],
    },
    {
        "description": "Path graph: two middle nodes",
        "run": lambda: sorted(solution(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])),
        "expected": [3, 4],
    },
    {
        "description": "Single node",
        "run": lambda: solution(1, []),
        "expected": [0],
    },
    {
        "description": "Two nodes",
        "run": lambda: sorted(solution(2, [[0, 1]])),
        "expected": [0, 1],
    },
]
