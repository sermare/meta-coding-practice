from problems.p381_number_of_connected_components import solution


TEST_CASES = [
    {
        "description": "Two components",
        "run": lambda: solution(5, [[0, 1], [1, 2], [3, 4]]),
        "expected": 2,
    },
    {
        "description": "One component (chain)",
        "run": lambda: solution(5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
        "expected": 1,
    },
    {
        "description": "All isolated",
        "run": lambda: solution(3, []),
        "expected": 3,
    },
    {
        "description": "Single node",
        "run": lambda: solution(1, []),
        "expected": 1,
    },
]
