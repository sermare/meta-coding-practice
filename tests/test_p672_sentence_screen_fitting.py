from problems.p672_sentence_screen_fitting import solution

TEST_CASES = [
    {
        "description": "hello world on 2x8 screen",
        "run": lambda: solution(["hello", "world"], 2, 8),
        "expected": 1,
    },
    {
        "description": "a bcd e on 3x6 screen",
        "run": lambda: solution(["a", "bcd", "e"], 3, 6),
        "expected": 2,
    },
    {
        "description": "Single word fits many times",
        "run": lambda: solution(["a"], 3, 3),
        "expected": 9,
    },
    {
        "description": "Word too long for screen",
        "run": lambda: solution(["hello"], 1, 3),
        "expected": 0,
    },
]
