from problems.p576_unique_word_abbreviation import solution

TEST_CASES = [
    {
        "description": "Mixed results",
        "run": lambda: solution(["deer", "door", "cake", "card"], ["dear", "cart", "cane", "make"]),
        "expected": [False, True, False, True],
    },
    {
        "description": "Word in dictionary is unique",
        "run": lambda: solution(["deer"], ["deer"]),
        "expected": [True],
    },
    {
        "description": "Empty dictionary",
        "run": lambda: solution([], ["hello"]),
        "expected": [True],
    },
    {
        "description": "Short words",
        "run": lambda: solution(["ab"], ["ab", "cd"]),
        "expected": [True, False],
    },
]
