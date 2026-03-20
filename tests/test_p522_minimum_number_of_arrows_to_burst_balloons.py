from problems.p522_minimum_number_of_arrows_to_burst_balloons import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([[10,16],[2,8],[1,6],[7,12]]),
        "expected": 2,
    },
    {
        "description": "Non-overlapping",
        "run": lambda: solution([[1,2],[3,4],[5,6],[7,8]]),
        "expected": 4,
    },
    {
        "description": "All overlap at one point",
        "run": lambda: solution([[1,5],[2,6],[3,7]]),
        "expected": 1,
    },
    {
        "description": "Single balloon",
        "run": lambda: solution([[1,5]]),
        "expected": 1,
    },
    {
        "description": "Touch at edge",
        "run": lambda: solution([[1,2],[2,3],[3,4]]),
        "expected": 2,
    },
]
