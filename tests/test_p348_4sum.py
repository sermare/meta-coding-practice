from problems.p348_4sum import solution

TEST_CASES = [
    {
        "description": "Basic: [1,0,-1,0,-2,2] target=0",
        "run": lambda: sorted([sorted(q) for q in solution([1, 0, -1, 0, -2, 2], 0)]),
        "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    },
    {
        "description": "All twos: [2,2,2,2,2] target=8",
        "run": lambda: solution([2, 2, 2, 2, 2], 8),
        "expected": [[2, 2, 2, 2]],
    },
    {
        "description": "No solution: [1,2,3,4] target=100",
        "run": lambda: solution([1, 2, 3, 4], 100),
        "expected": [],
    },
    {
        "description": "Empty: [] target=0",
        "run": lambda: solution([], 0),
        "expected": [],
    },
]
