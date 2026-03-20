from problems.p691_implement_magic_dictionary import solution

TEST_CASES = [
    {
        "description": "Basic magic dictionary operations",
        "run": lambda: solution(["hello", "leetcode"], ["hello", "hhllo", "hell", "leetcoded"]),
        "expected": [False, True, False, False],
    },
    {
        "description": "Single char words",
        "run": lambda: solution(["a", "b"], ["c", "a"]),
        "expected": [True, True],
    },
    {
        "description": "No matches possible",
        "run": lambda: solution(["abc"], ["xyz", "ab", "abcd"]),
        "expected": [False, False, False],
    },
    {
        "description": "Empty dictionary",
        "run": lambda: solution([], ["hello"]),
        "expected": [False],
    },
]
