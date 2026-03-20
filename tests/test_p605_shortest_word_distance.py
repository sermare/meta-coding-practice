from problems.p605_shortest_word_distance import solution

TEST_CASES = [
    {
        "description": "Basic case: coding and practice",
        "run": lambda: solution(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"),
        "expected": 3,
    },
    {
        "description": "Adjacent words: makes and coding",
        "run": lambda: solution(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"),
        "expected": 1,
    },
    {
        "description": "Two words only",
        "run": lambda: solution(["a", "b"], "a", "b"),
        "expected": 1,
    },
    {
        "description": "Multiple occurrences",
        "run": lambda: solution(["a", "c", "b", "a"], "a", "b"),
        "expected": 1,
    },
]
