from problems.p708_word_frequency import solution

TEST_CASES = [
    {
        "description": "Basic frequency count",
        "run": lambda: solution(["the", "day", "is", "sunny", "the", "the", "sunny", "is", "is"]),
        "expected": {"the": 3, "is": 3, "sunny": 2, "day": 1},
    },
    {
        "description": "Single word repeated",
        "run": lambda: solution(["hello", "hello", "hello"]),
        "expected": {"hello": 3},
    },
    {
        "description": "All unique words",
        "run": lambda: solution(["a", "b", "c"]),
        "expected": {"a": 1, "b": 1, "c": 1},
    },
    {
        "description": "Empty list",
        "run": lambda: solution([]),
        "expected": {},
    },
    {
        "description": "Single word",
        "run": lambda: solution(["word"]),
        "expected": {"word": 1},
    },
]
