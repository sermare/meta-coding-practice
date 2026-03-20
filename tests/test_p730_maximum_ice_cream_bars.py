from problems.p730_maximum_ice_cream_bars import solution

TEST_CASES = [
    {
        "description": "Basic case: costs=[1,3,2,4,1], coins=7",
        "run": lambda: solution([1, 3, 2, 4, 1], 7),
        "expected": 4,
    },
    {
        "description": "Can buy all: costs=[1,1,1], coins=5",
        "run": lambda: solution([1, 1, 1], 5),
        "expected": 3,
    },
    {
        "description": "Cannot buy any: costs=[10,20], coins=5",
        "run": lambda: solution([10, 20], 5),
        "expected": 0,
    },
    {
        "description": "Exact coins: costs=[1,2,3], coins=6",
        "run": lambda: solution([1, 2, 3], 6),
        "expected": 3,
    },
]
