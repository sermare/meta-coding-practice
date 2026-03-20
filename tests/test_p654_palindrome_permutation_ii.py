from problems.p654_palindrome_permutation_ii import solution

TEST_CASES = [
    {
        "description": "Two palindrome permutations: aabb",
        "run": lambda: sorted(solution("aabb")),
        "expected": ["abba", "baab"],
    },
    {
        "description": "No palindrome permutation: abc",
        "run": lambda: solution("abc"),
        "expected": [],
    },
    {
        "description": "Single character: a",
        "run": lambda: solution("a"),
        "expected": ["a"],
    },
    {
        "description": "Odd-length palindrome: aab",
        "run": lambda: sorted(solution("aab")),
        "expected": ["aba"],
    },
]
