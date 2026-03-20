from problems.p529_partition_labels import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution("ababcbacadefegdehijhklij"),
        "expected": [9, 7, 8],
    },
    {
        "description": "Single chars",
        "run": lambda: solution("abc"),
        "expected": [1, 1, 1],
    },
    {
        "description": "One partition",
        "run": lambda: solution("abab"),
        "expected": [4],
    },
    {
        "description": "Single char string",
        "run": lambda: solution("a"),
        "expected": [1],
    },
    {
        "description": "Repeated pattern",
        "run": lambda: solution("eccbbbbdec"),
        "expected": [10],
    },
]
