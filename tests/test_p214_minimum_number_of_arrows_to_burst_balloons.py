from problems.p214_minimum_number_of_arrows_to_burst_balloons import solution

TEST_CASES = [
    {
        "description": "Overlapping: [[10,16],[2,8],[1,6],[7,12]]",
        "run": lambda: solution([[10, 16], [2, 8], [1, 6], [7, 12]]),
        "expected": 2,
    },
    {
        "description": "No overlap: [[1,2],[3,4],[5,6],[7,8]]",
        "run": lambda: solution([[1, 2], [3, 4], [5, 6], [7, 8]]),
        "expected": 4,
    },
    {
        "description": "All overlap: [[1,6],[2,8],[3,10]]",
        "run": lambda: solution([[1, 6], [2, 8], [3, 10]]),
        "expected": 1,
    },
    {
        "description": "Single balloon",
        "run": lambda: solution([[1, 2]]),
        "expected": 1,
    },
    {
        "description": "Touching edges: [[1,2],[2,3],[3,4]]",
        "run": lambda: solution([[1, 2], [2, 3], [3, 4]]),
        "expected": 2,
    },
]
