from problems.p483_koko_eating_bananas import solution

TEST_CASES = [
    {
        "description": "Standard: [3,6,7,11] h=8 -> 4",
        "run": lambda: solution([3,6,7,11], 8),
        "expected": 4,
    },
    {
        "description": "Exact hours: [30,11,23,4,20] h=5 -> 30",
        "run": lambda: solution([30,11,23,4,20], 5),
        "expected": 30,
    },
    {
        "description": "Extra hour: [30,11,23,4,20] h=6 -> 23",
        "run": lambda: solution([30,11,23,4,20], 6),
        "expected": 23,
    },
    {
        "description": "Single pile: [10] h=5 -> 2",
        "run": lambda: solution([10], 5),
        "expected": 2,
    },
    {
        "description": "Large h: [1,1,1] h=100 -> 1",
        "run": lambda: solution([1,1,1], 100),
        "expected": 1,
    },
]
