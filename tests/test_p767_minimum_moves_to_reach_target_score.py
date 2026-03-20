from problems.p767_minimum_moves_to_reach_target_score import solution

TEST_CASES = [
    {
        "description": "target=19, maxDoubles=2",
        "run": lambda: solution(19, 2),
        "expected": 7,
    },
    {
        "description": "target=5, maxDoubles=0",
        "run": lambda: solution(5, 0),
        "expected": 4,
    },
    {
        "description": "target=10, maxDoubles=4",
        "run": lambda: solution(10, 4),
        "expected": 4,
    },
    {
        "description": "target=1, maxDoubles=1",
        "run": lambda: solution(1, 1),
        "expected": 0,
    },
]
