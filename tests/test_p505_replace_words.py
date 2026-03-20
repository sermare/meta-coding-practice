from problems.p505_replace_words import solution

TEST_CASES = [
    {
        "description": "Basic replacement",
        "run": lambda: solution(["cat","bat","rat"], "the cattle was rattled by the battery"),
        "expected": "the cat was rat by the bat",
    },
    {
        "description": "No replacement needed",
        "run": lambda: solution(["abc"], "hello world"),
        "expected": "hello world",
    },
    {
        "description": "Shortest root wins",
        "run": lambda: solution(["a","ab","abc"], "abcdef"),
        "expected": "a",
    },
    {
        "description": "Multiple roots same word",
        "run": lambda: solution(["cat","cater"], "caterpillar"),
        "expected": "cat",
    },
    {
        "description": "Empty dictionary",
        "run": lambda: solution([], "hello world"),
        "expected": "hello world",
    },
]
