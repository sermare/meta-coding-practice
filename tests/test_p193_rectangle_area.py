from problems.p193_rectangle_area import solution

TEST_CASES = [
    {
        "description": "Overlapping rectangles -> 45",
        "run": lambda: solution(-3, 0, 3, 4, 0, -1, 9, 2),
        "expected": 45,
    },
    {
        "description": "No overlap",
        "run": lambda: solution(-2, -2, 2, 2, 3, 3, 4, 4),
        "expected": 17,
    },
    {
        "description": "Same rectangle",
        "run": lambda: solution(0, 0, 2, 2, 0, 0, 2, 2),
        "expected": 4,
    },
    {
        "description": "One inside other",
        "run": lambda: solution(-3, -3, 3, 3, -1, -1, 1, 1),
        "expected": 36,
    },
]
