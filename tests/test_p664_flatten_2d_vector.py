from problems.p664_flatten_2d_vector import solution

TEST_CASES = [
    {
        "description": "Basic 2D vector: [[1,2],[3],[4]]",
        "run": lambda: solution([[1, 2], [3], [4]]),
        "expected": [1, 2, 3, 4],
    },
    {
        "description": "Empty inner lists: [[],[1],[]]",
        "run": lambda: solution([[], [1], []]),
        "expected": [1],
    },
    {
        "description": "Single list: [[1,2,3]]",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": [1, 2, 3],
    },
    {
        "description": "All empty: [[],[],[]]",
        "run": lambda: solution([[], [], []]),
        "expected": [],
    },
    {
        "description": "Empty input",
        "run": lambda: solution([]),
        "expected": [],
    },
]
