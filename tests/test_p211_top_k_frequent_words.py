from problems.p211_top_k_frequent_words import solution

TEST_CASES = [
    {
        "description": "Basic: k=2",
        "run": lambda: solution(["i", "love", "leetcode", "i", "love", "coding"], 2),
        "expected": ["i", "love"],
    },
    {
        "description": "Ties broken lexicographically: k=4",
        "run": lambda: solution(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        "expected": ["the", "is", "sunny", "day"],
    },
    {
        "description": "Single word: k=1",
        "run": lambda: solution(["hello"], 1),
        "expected": ["hello"],
    },
    {
        "description": "All same frequency: k=2",
        "run": lambda: solution(["a", "b", "c"], 2),
        "expected": ["a", "b"],
    },
]
