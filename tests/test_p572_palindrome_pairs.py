from problems.p572_palindrome_pairs import solution

TEST_CASES = [
    {
        "description": "Multiple pairs",
        "run": lambda: sorted(solution(["abcd", "dcba", "lls", "s", "sssll"])),
        "expected": sorted([[0, 1], [1, 0], [3, 2], [2, 4]]),
    },
    {
        "description": "Simple reversal: bat, tab",
        "run": lambda: sorted(solution(["bat", "tab", "cat"])),
        "expected": sorted([[0, 1], [1, 0]]),
    },
    {
        "description": "Empty string present",
        "run": lambda: sorted(solution(["a", ""])),
        "expected": sorted([[0, 1], [1, 0]]),
    },
    {
        "description": "No pairs",
        "run": lambda: solution(["abc", "def"]),
        "expected": [],
    },
]
