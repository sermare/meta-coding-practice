from problems.p606_shortest_word_distance_ii import solution

TEST_CASES = [
    {
        "description": "Single query: coding and practice",
        "run": lambda: solution(
            ["practice", "makes", "perfect", "coding", "makes"],
            [("coding", "practice")]
        ),
        "expected": [3],
    },
    {
        "description": "Single query: makes and coding",
        "run": lambda: solution(
            ["practice", "makes", "perfect", "coding", "makes"],
            [("makes", "coding")]
        ),
        "expected": [1],
    },
    {
        "description": "Multiple queries",
        "run": lambda: solution(
            ["practice", "makes", "perfect", "coding", "makes"],
            [("coding", "practice"), ("makes", "coding")]
        ),
        "expected": [3, 1],
    },
    {
        "description": "Two element dict",
        "run": lambda: solution(["a", "b"], [("a", "b")]),
        "expected": [1],
    },
]
