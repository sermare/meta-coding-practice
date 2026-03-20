from problems.p132_reorganize_string import solution

def is_valid_reorganize(result, original):
    """Check if result is a valid reorganization of original."""
    if result == "":
        return True
    if sorted(result) != sorted(original):
        return False
    for i in range(1, len(result)):
        if result[i] == result[i-1]:
            return False
    return True

TEST_CASES = [
    {
        "description": "Possible reorganization",
        "run": lambda: is_valid_reorganize(solution("aab"), "aab"),
        "expected": True,
    },
    {
        "description": "Impossible reorganization",
        "run": lambda: solution("aaab"),
        "expected": "",
    },
    {
        "description": "Single character",
        "run": lambda: solution("a"),
        "expected": "a",
    },
    {
        "description": "Two different chars",
        "run": lambda: is_valid_reorganize(solution("aabb"), "aabb"),
        "expected": True,
    },
    {
        "description": "Already valid",
        "run": lambda: is_valid_reorganize(solution("abc"), "abc"),
        "expected": True,
    },
]
