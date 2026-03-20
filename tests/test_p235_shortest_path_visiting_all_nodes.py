from problems.p235_shortest_path_visiting_all_nodes import solution

TEST_CASES = [
    {
        "description": "Star graph: [[1,2,3],[0],[0],[0]]",
        "run": lambda: solution([[1, 2, 3], [0], [0], [0]]),
        "expected": 4,
    },
    {
        "description": "Connected: [[1],[0,2,4],[1,3,4],[2],[1,2]]",
        "run": lambda: solution([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]),
        "expected": 4,
    },
    {
        "description": "Single node: [[]]",
        "run": lambda: solution([[]]),
        "expected": 0,
    },
    {
        "description": "Two nodes: [[1],[0]]",
        "run": lambda: solution([[1], [0]]),
        "expected": 1,
    },
]
