from problems.p031_custom_sort_string import solution

def _is_valid_custom_sort(order, s, result):
    """Check that result is a valid custom sort of s according to order."""
    if result is None:
        return False
    # result must be a permutation of s
    if sorted(result) != sorted(s):
        return False
    # Characters in order must appear in the correct relative order in result
    order_index = {c: i for i, c in enumerate(order)}
    filtered = [c for c in result if c in order_index]
    for i in range(len(filtered) - 1):
        if order_index[filtered[i]] > order_index[filtered[i + 1]]:
            return False
    return True

TEST_CASES = [
    {
        "description": "Basic case: order='cba', s='abcd' -> 'cbad'",
        "run": lambda: (
            _is_valid_custom_sort("cba", "abcd", solution("cba", "abcd"))
        ),
        "expected": True,
    },
    {
        "description": "order='bcafg', s='abcd' -> 'bcad'",
        "run": lambda: (
            _is_valid_custom_sort("bcafg", "abcd", solution("bcafg", "abcd"))
        ),
        "expected": True,
    },
    {
        "description": "order='kqep', s='pekeq' -> valid custom sort",
        "run": lambda: (
            _is_valid_custom_sort("kqep", "pekeq", solution("kqep", "pekeq"))
        ),
        "expected": True,
    },
    {
        "description": "Characters not in order: order='xyz', s='abc' -> 'abc' (any order fine)",
        "run": lambda: (
            _is_valid_custom_sort("xyz", "abc", solution("xyz", "abc"))
        ),
        "expected": True,
    },
    {
        "description": "Empty order: order='', s='abc' -> 'abc' (any permutation)",
        "run": lambda: (
            _is_valid_custom_sort("", "abc", solution("", "abc"))
        ),
        "expected": True,
    },
]
