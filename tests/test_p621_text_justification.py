from problems.p621_text_justification import solution

TEST_CASES = [
    {
        "description": "Standard justification",
        "run": lambda: solution(["This", "is", "an", "example", "of", "text", "justification."], 16),
        "expected": ["This    is    an", "example  of text", "justification.  "],
    },
    {
        "description": "What must be acknowledgement shall be",
        "run": lambda: solution(["What", "must", "be", "acknowledgment", "shall", "be"], 16),
        "expected": ["What   must   be", "acknowledgment  ", "shall be        "],
    },
    {
        "description": "Single word per line",
        "run": lambda: solution(["a"], 1),
        "expected": ["a"],
    },
    {
        "description": "Single long word",
        "run": lambda: solution(["hello"], 10),
        "expected": ["hello     "],
    },
]
