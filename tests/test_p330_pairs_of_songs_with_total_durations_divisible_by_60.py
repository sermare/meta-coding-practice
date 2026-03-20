from problems.p330_pairs_of_songs_with_total_durations_divisible_by_60 import solution

TEST_CASES = [
    {
        "description": "Basic: [30,20,150,100,40] -> 3",
        "run": lambda: solution([30, 20, 150, 100, 40]),
        "expected": 3,
    },
    {
        "description": "All 60: [60,60,60] -> 3",
        "run": lambda: solution([60, 60, 60]),
        "expected": 3,
    },
    {
        "description": "No pairs: [10,20] -> 0",
        "run": lambda: solution([10, 20]),
        "expected": 0,
    },
    {
        "description": "Single song: [30] -> 0",
        "run": lambda: solution([30]),
        "expected": 0,
    },
]
