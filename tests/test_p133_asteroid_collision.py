from problems.p133_asteroid_collision import solution

TEST_CASES = [
    {
        "description": "Larger asteroid survives",
        "run": lambda: solution([5, 10, -5]),
        "expected": [5, 10],
    },
    {
        "description": "Equal size both explode",
        "run": lambda: solution([8, -8]),
        "expected": [],
    },
    {
        "description": "No collision (same direction)",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Left moving destroys all",
        "run": lambda: solution([10, 2, -5]),
        "expected": [10],
    },
    {
        "description": "Chain of collisions",
        "run": lambda: solution([-2, -1, 1, 2]),
        "expected": [-2, -1, 1, 2],
    },
]
