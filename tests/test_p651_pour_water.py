from problems.p651_pour_water import solution

TEST_CASES = [
    {
        "description": "Basic valley fill: V=4, K=3",
        "run": lambda: solution([2, 1, 1, 2, 1, 2, 2], 4, 3),
        "expected": [2, 2, 2, 3, 2, 2, 2],
    },
    {
        "description": "Single drop at edge: V=1, K=0",
        "run": lambda: solution([1, 2, 3], 1, 0),
        "expected": [2, 2, 3],
    },
    {
        "description": "Flat terrain: V=2, K=1",
        "run": lambda: solution([3, 3, 3], 2, 1),
        "expected": [3, 5, 3],
    },
    {
        "description": "Water flows left: V=1, K=2",
        "run": lambda: solution([3, 1, 2, 3], 1, 2),
        "expected": [3, 2, 2, 3],
    },
    {
        "description": "No flow possible: V=3, K=0",
        "run": lambda: solution([5], 3, 0),
        "expected": [8],
    },
]
