from problems.p470_daily_temperatures import solution

TEST_CASES = [
    {
        "description": "Standard case",
        "run": lambda: solution([73,74,75,71,69,72,76,73]),
        "expected": [1,1,4,2,1,1,0,0],
    },
    {
        "description": "Increasing: [30,40,50,60]",
        "run": lambda: solution([30,40,50,60]),
        "expected": [1,1,1,0],
    },
    {
        "description": "Short: [30,60,90]",
        "run": lambda: solution([30,60,90]),
        "expected": [1,1,0],
    },
    {
        "description": "All same: [50,50,50]",
        "run": lambda: solution([50,50,50]),
        "expected": [0,0,0],
    },
    {
        "description": "Decreasing: [90,80,70]",
        "run": lambda: solution([90,80,70]),
        "expected": [0,0,0],
    },
]
