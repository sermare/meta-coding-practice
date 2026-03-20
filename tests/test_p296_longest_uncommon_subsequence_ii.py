from problems.p296_longest_uncommon_subsequence_ii import solution

TEST_CASES = [
    {
        "description": "['aba','cdc','eae'] -> 3",
        "run": lambda: solution(["aba", "cdc", "eae"]),
        "expected": 3,
    },
    {
        "description": "['aaa','aaa','aa'] -> -1",
        "run": lambda: solution(["aaa", "aaa", "aa"]),
        "expected": -1,
    },
    {
        "description": "['a','b','c'] -> 1",
        "run": lambda: solution(["a", "b", "c"]),
        "expected": 1,
    },
    {
        "description": "['aabbcc','aabbcc','cb'] -> -1",
        "run": lambda: solution(["aabbcc", "aabbcc", "cb"]),
        "expected": 2,
    },
    {
        "description": "['abc','def'] -> 3",
        "run": lambda: solution(["abc", "def"]),
        "expected": 3,
    },
]
