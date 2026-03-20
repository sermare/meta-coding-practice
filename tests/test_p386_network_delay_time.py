from problems.p386_network_delay_time import solution


TEST_CASES = [
    {
        "description": "Signal reaches all in 2 units",
        "run": lambda: solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
        "expected": 2,
    },
    {
        "description": "Direct edge only",
        "run": lambda: solution([[1, 2, 1]], 2, 1),
        "expected": 1,
    },
    {
        "description": "Unreachable node",
        "run": lambda: solution([[1, 2, 1]], 2, 2),
        "expected": -1,
    },
    {
        "description": "Single node",
        "run": lambda: solution([], 1, 1),
        "expected": 0,
    },
]
