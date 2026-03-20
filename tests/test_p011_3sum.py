from problems.p011_3sum import solution


def _normalize(result):
    """Sort each triplet and then sort the list of triplets for order-independent comparison."""
    if result is None:
        return None
    return sorted([sorted(triplet) for triplet in result])


TEST_CASES = [
    {
        "description": "Example with multiple triplets: [-1,0,1,2,-1,-4]",
        "run": lambda: _normalize(solution([-1, 0, 1, 2, -1, -4])),
        "expected": _normalize([[-1, -1, 2], [-1, 0, 1]]),
    },
    {
        "description": "No triplets sum to zero: [0,1,1]",
        "run": lambda: _normalize(solution([0, 1, 1])),
        "expected": _normalize([]),
    },
    {
        "description": "All zeros: [0,0,0]",
        "run": lambda: _normalize(solution([0, 0, 0])),
        "expected": _normalize([[0, 0, 0]]),
    },
    {
        "description": "Two triplets: [-2,0,1,1,2]",
        "run": lambda: _normalize(solution([-2, 0, 1, 1, 2])),
        "expected": _normalize([[-2, 0, 2], [-2, 1, 1]]),
    },
    {
        "description": "Duplicate elements: [1,-1,-1,0]",
        "run": lambda: _normalize(solution([1, -1, -1, 0])),
        "expected": _normalize([[-1, 0, 1]]),
    },
]
