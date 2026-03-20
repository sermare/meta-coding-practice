from problems.p757_truncate_sentence import solution

TEST_CASES = [
    {
        "description": "Truncate to 4 words",
        "run": lambda: solution("Hello how are you Contestant", 4),
        "expected": "Hello how are you",
    },
    {
        "description": "Truncate to 1 word",
        "run": lambda: solution("What is the solution to this problem", 1),
        "expected": "What",
    },
    {
        "description": "Keep all words",
        "run": lambda: solution("hello world", 2),
        "expected": "hello world",
    },
    {
        "description": "Truncate to 5 words",
        "run": lambda: solution("chopper is not a dinosaur", 5),
        "expected": "chopper is not a dinosaur",
    },
]
