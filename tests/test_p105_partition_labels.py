from problems.p105_partition_labels import solution

TEST_CASES = [
    {
        "description": "Standard partition example",
        "run": lambda: solution("ababcbacadefegdehijhklij"),
        "expected": [9, 7, 8],
    },
    {
        "description": "All same characters",
        "run": lambda: solution("aaaa"),
        "expected": [4],
    },
    {
        "description": "Each character unique",
        "run": lambda: solution("abcdef"),
        "expected": [1, 1, 1, 1, 1, 1],
    },
    {
        "description": "Two partitions",
        "run": lambda: solution("eccbbbbdec"),
        "expected": [10],
    },
    {
        "description": "Single character",
        "run": lambda: solution("a"),
        "expected": [1],
    },
]
