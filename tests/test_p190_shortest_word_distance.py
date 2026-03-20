from problems.p190_shortest_word_distance import solution

TEST_CASES = [
    {
        "description": "coding to practice -> 3",
        "run": lambda: solution(["practice","makes","perfect","coding","makes"], "coding", "practice"),
        "expected": 3,
    },
    {
        "description": "makes to coding -> 1",
        "run": lambda: solution(["practice","makes","perfect","coding","makes"], "makes", "coding"),
        "expected": 1,
    },
    {
        "description": "Adjacent words",
        "run": lambda: solution(["a", "b"], "a", "b"),
        "expected": 1,
    },
    {
        "description": "Multiple occurrences pick closest",
        "run": lambda: solution(["a","c","b","a"], "a", "b"),
        "expected": 1,
    },
]
