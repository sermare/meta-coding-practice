from problems.p806_shortest_common_supersequence import solution

TEST_CASES = [
    {
        "description": "abac and cab",
        "run": lambda: len(solution("abac", "cab")),
        "expected": 5,
    },
    {
        "description": "Same strings: abc and abc",
        "run": lambda: solution("abc", "abc"),
        "expected": "abc",
    },
    {
        "description": "No overlap: ab and cd",
        "run": lambda: len(solution("ab", "cd")),
        "expected": 4,
    },
    {
        "description": "One empty: abc and empty",
        "run": lambda: solution("abc", ""),
        "expected": "abc",
    },
]
