from problems.p506_longest_word_in_dictionary import solution

TEST_CASES = [
    {
        "description": "Build one char at a time",
        "run": lambda: solution(["w","wo","wor","worl","world"]),
        "expected": "world",
    },
    {
        "description": "Lexicographically smallest",
        "run": lambda: solution(["a","banana","app","appl","ap","apply","apple"]),
        "expected": "apple",
    },
    {
        "description": "Single char words",
        "run": lambda: solution(["a","b","c"]),
        "expected": "a",
    },
    {
        "description": "No buildable word",
        "run": lambda: solution(["abc","def"]),
        "expected": "",
    },
    {
        "description": "Tie breaking",
        "run": lambda: solution(["a","ab","b","bc"]),
        "expected": "ab",
    },
]
