from problems.p102_most_common_word import solution

TEST_CASES = [
    {
        "description": "Standard example with banned word",
        "run": lambda: solution("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
        "expected": "ball",
    },
    {
        "description": "Single word, no banned",
        "run": lambda: solution("a.", []),
        "expected": "a",
    },
    {
        "description": "Multiple banned words",
        "run": lambda: solution("a a a b b c c c d", ["a", "c"]),
        "expected": "b",
    },
    {
        "description": "Case insensitive comparison",
        "run": lambda: solution("Bob. hIt, baLl", ["bob"]),
        "expected": "hit",
    },
    {
        "description": "Punctuation heavy",
        "run": lambda: solution("apple! apple? APPLE, banana", []),
        "expected": "apple",
    },
]
