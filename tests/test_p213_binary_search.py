from problems.p213_binary_search import solution

TEST_CASES = [
    {
        "description": "Found: target=9 in [-1,0,3,5,9,12]",
        "run": lambda: solution([-1, 0, 3, 5, 9, 12], 9),
        "expected": 4,
    },
    {
        "description": "Not found: target=2",
        "run": lambda: solution([-1, 0, 3, 5, 9, 12], 2),
        "expected": -1,
    },
    {
        "description": "Single element found: [5] target=5",
        "run": lambda: solution([5], 5),
        "expected": 0,
    },
    {
        "description": "Single element not found: [5] target=1",
        "run": lambda: solution([5], 1),
        "expected": -1,
    },
    {
        "description": "First element: target=-1",
        "run": lambda: solution([-1, 0, 3, 5, 9, 12], -1),
        "expected": 0,
    },
]
