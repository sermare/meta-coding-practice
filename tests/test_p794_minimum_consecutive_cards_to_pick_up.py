from problems.p794_minimum_consecutive_cards_to_pick_up import solution

TEST_CASES = [
    {
        "description": "Basic: [3,4,2,3,4,7]",
        "run": lambda: solution([3,4,2,3,4,7]),
        "expected": 4,
    },
    {
        "description": "No matching pair: [1,0,5,3]",
        "run": lambda: solution([1,0,5,3]),
        "expected": -1,
    },
    {
        "description": "Adjacent pair: [1,1]",
        "run": lambda: solution([1,1]),
        "expected": 2,
    },
    {
        "description": "Multiple options: [0,0,0]",
        "run": lambda: solution([0,0,0]),
        "expected": 2,
    },
]
