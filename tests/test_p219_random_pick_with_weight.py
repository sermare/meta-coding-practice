from problems.p219_random_pick_with_weight import solution

TEST_CASES = [
    {
        "description": "Single weight: [1] should always return 0",
        "run": lambda: all(x == 0 for x in (solution([1], 100) or [])) if solution([1], 100) is not None else None,
        "expected": True,
    },
    {
        "description": "Two weights: [1,3] index 1 should be more frequent",
        "run": lambda: (lambda r: r is not None and sum(1 for x in r if x == 1) > sum(1 for x in r if x == 0))(solution([1, 3], 1000)) if solution([1, 3], 1000) is not None else None,
        "expected": True,
    },
    {
        "description": "Equal weights: [1,1,1] all indices should appear",
        "run": lambda: (lambda r: r is not None and len(set(r)) == 3)(solution([1, 1, 1], 1000)) if solution([1, 1, 1], 1000) is not None else None,
        "expected": True,
    },
    {
        "description": "Result length matches num_picks",
        "run": lambda: len(solution([2, 5], 50)) if solution([2, 5], 50) is not None else None,
        "expected": 50,
    },
]
