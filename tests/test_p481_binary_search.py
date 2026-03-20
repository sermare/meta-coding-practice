from problems.p481_binary_search import solution

TEST_CASES = [
    {
        "description": "Found: target=9 -> index 4",
        "run": lambda: solution([-1,0,3,5,9,12], 9),
        "expected": 4,
    },
    {
        "description": "Not found: target=2 -> -1",
        "run": lambda: solution([-1,0,3,5,9,12], 2),
        "expected": -1,
    },
    {
        "description": "First element",
        "run": lambda: solution([1,2,3,4,5], 1),
        "expected": 0,
    },
    {
        "description": "Last element",
        "run": lambda: solution([1,2,3,4,5], 5),
        "expected": 4,
    },
    {
        "description": "Single element found",
        "run": lambda: solution([5], 5),
        "expected": 0,
    },
]
