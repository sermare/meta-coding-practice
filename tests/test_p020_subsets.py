from problems.p020_subsets import solution


def _normalize(result):
    """Sort each subset and then sort all subsets for order-independent comparison."""
    if result is None:
        return None
    return sorted([sorted(subset) for subset in result])


TEST_CASES = [
    {
        "description": "Subsets of [1,2,3]",
        "run": lambda: _normalize(solution([1, 2, 3])),
        "expected": _normalize([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    },
    {
        "description": "Subsets of [0]",
        "run": lambda: _normalize(solution([0])),
        "expected": _normalize([[], [0]]),
    },
    {
        "description": "Subsets of [1,2]",
        "run": lambda: _normalize(solution([1, 2])),
        "expected": _normalize([[], [1], [2], [1, 2]]),
    },
]
