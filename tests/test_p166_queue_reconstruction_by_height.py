from problems.p166_queue_reconstruction_by_height import solution

TEST_CASES = [
    {
        "description": "Standard case",
        "run": lambda: solution([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]),
        "expected": [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]],
    },
    {
        "description": "Already sorted",
        "run": lambda: solution([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]),
        "expected": [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]],
    },
    {
        "description": "Single person",
        "run": lambda: solution([[7, 0]]),
        "expected": [[7, 0]],
    },
    {
        "description": "Two people",
        "run": lambda: solution([[7, 0], [7, 1]]),
        "expected": [[7, 0], [7, 1]],
    },
]
