from problems.p129_snakes_and_ladders import solution

TEST_CASES = [
    {
        "description": "Standard 6x6 board",
        "run": lambda: solution([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]),
        "expected": 4,
    },
    {
        "description": "No snakes or ladders, 2x2",
        "run": lambda: solution([[-1,-1],[-1,-1]]),
        "expected": 1,
    },
    {
        "description": "Simple ladder helps",
        "run": lambda: solution([[-1,-1,-1],[-1,-1,-1],[-1,9,-1]]),
        "expected": 1,
    },
    {
        "description": "Already at end impossible (1x1 not valid, use 2x2)",
        "run": lambda: solution([[-1,4],[-1,-1]]),
        "expected": 1,
    },
]
