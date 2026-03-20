from problems.p497_find_right_interval import solution

TEST_CASES = [
    {
        "description": "Single interval: [[1,2]] -> [-1]",
        "run": lambda: solution([[1,2]]),
        "expected": [-1],
    },
    {
        "description": "Three intervals: [[3,4],[2,3],[1,2]]",
        "run": lambda: solution([[3,4],[2,3],[1,2]]),
        "expected": [-1,0,1],
    },
    {
        "description": "Overlapping: [[1,4],[2,3],[3,4]]",
        "run": lambda: solution([[1,4],[2,3],[3,4]]),
        "expected": [-1,2,2],
    },
    {
        "description": "Self-referencing: [[1,1]]",
        "run": lambda: solution([[1,1]]),
        "expected": [0],
    },
    {
        "description": "Two intervals: [[1,2],[2,3]]",
        "run": lambda: solution([[1,2],[2,3]]),
        "expected": [1,-1],
    },
]
