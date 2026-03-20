from problems.p081_network_delay_time import solution

TEST_CASES = [
    {
        "description": "Standard: 4 nodes from node 2",
        "run": lambda: solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
        "expected": 2,
    },
    {
        "description": "Simple: 2 nodes from node 1",
        "run": lambda: solution([[1, 2, 1]], 2, 1),
        "expected": 1,
    },
    {
        "description": "Unreachable: 2 nodes from node 2",
        "run": lambda: solution([[1, 2, 1]], 2, 2),
        "expected": -1,
    },
    {
        "description": "Single node",
        "run": lambda: solution([], 1, 1),
        "expected": 0,
    },
]
