from problems.p698_teemo_attacking import solution

TEST_CASES = [
    {
        "description": "Non-overlapping: [1,4] duration=2",
        "run": lambda: solution([1, 4], 2),
        "expected": 4,
    },
    {
        "description": "Overlapping: [1,2] duration=2",
        "run": lambda: solution([1, 2], 2),
        "expected": 3,
    },
    {
        "description": "Single attack",
        "run": lambda: solution([1], 5),
        "expected": 5,
    },
    {
        "description": "No attacks",
        "run": lambda: solution([], 3),
        "expected": 0,
    },
    {
        "description": "All overlapping: [1,2,3,4] duration=5",
        "run": lambda: solution([1, 2, 3, 4], 5),
        "expected": 8,
    },
]
