from problems.p559_invalid_transactions import solution

TEST_CASES = [
    {
        "description": "Different city within 60 min",
        "run": lambda: sorted(solution(["alice,20,800,mtv", "alice,50,100,beijing"])),
        "expected": sorted(["alice,20,800,mtv", "alice,50,100,beijing"]),
    },
    {
        "description": "Amount over 1000",
        "run": lambda: solution(["alice,20,800,mtv", "alice,50,1200,mtv"]),
        "expected": ["alice,50,1200,mtv"],
    },
    {
        "description": "All valid",
        "run": lambda: solution(["alice,20,800,mtv", "bob,50,100,beijing"]),
        "expected": [],
    },
    {
        "description": "Same city, different name within 60 min",
        "run": lambda: solution(["alice,20,800,mtv", "bob,50,100,mtv"]),
        "expected": [],
    },
]
