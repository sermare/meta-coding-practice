from problems.p013_group_anagrams import solution


def _normalize(result):
    """Sort each group internally and then sort all groups for order-independent comparison."""
    if result is None:
        return None
    return sorted([sorted(group) for group in result])


TEST_CASES = [
    {
        "description": "Multiple anagram groups",
        "run": lambda: _normalize(solution(["eat", "tea", "tan", "ate", "nat", "bat"])),
        "expected": _normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    },
    {
        "description": "Single empty string",
        "run": lambda: _normalize(solution([""])),
        "expected": _normalize([[""]]),
    },
    {
        "description": "Single character string",
        "run": lambda: _normalize(solution(["a"])),
        "expected": _normalize([["a"]]),
    },
]
