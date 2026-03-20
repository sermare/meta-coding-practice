from problems.p499_minimum_speed_to_arrive_on_time import solution

TEST_CASES = [
    {
        "description": "Slow speed: [1,3,2] hour=6 -> 1",
        "run": lambda: solution([1,3,2], 6),
        "expected": 1,
    },
    {
        "description": "Faster: [1,3,2] hour=2.7 -> 3",
        "run": lambda: solution([1,3,2], 2.7),
        "expected": 3,
    },
    {
        "description": "Impossible: [1,3,2] hour=1.9 -> -1",
        "run": lambda: solution([1,3,2], 1.9),
        "expected": -1,
    },
    {
        "description": "Single train: [10] hour=5 -> 2",
        "run": lambda: solution([10], 5),
        "expected": 2,
    },
    {
        "description": "Exact: [1,1,1] hour=3 -> 1",
        "run": lambda: solution([1,1,1], 3),
        "expected": 1,
    },
]
