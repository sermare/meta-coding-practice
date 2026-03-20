from problems.p440_n-queens import solution

TEST_CASES = [
    {
        "description": "n=4",
        "run": lambda: sorted(solution(4)),
        "expected": sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": [["Q"]],
    },
    {
        "description": "n=2 (no solution)",
        "run": lambda: solution(2),
        "expected": [],
    },
    {
        "description": "n=3 (no solution)",
        "run": lambda: solution(3),
        "expected": [],
    },
    {
        "description": "Count for n=5",
        "run": lambda: len(solution(5)),
        "expected": 10,
    },
]
