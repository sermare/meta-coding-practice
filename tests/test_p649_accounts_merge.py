from problems.p649_accounts_merge import solution

TEST_CASES = [
    {
        "description": "Merge shared accounts",
        "run": lambda: sorted([sorted(a) for a in solution([
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ])]),
        "expected": sorted([
            sorted(["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]),
            sorted(["John", "johnnybravo@mail.com"]),
            sorted(["Mary", "mary@mail.com"])
        ]),
    },
    {
        "description": "No merge needed",
        "run": lambda: sorted([sorted(a) for a in solution([
            ["A", "a@b.com"],
            ["B", "b@b.com"]
        ])]),
        "expected": sorted([sorted(["A", "a@b.com"]), sorted(["B", "b@b.com"])]),
    },
    {
        "description": "Single account",
        "run": lambda: solution([["Alice", "alice@mail.com"]]),
        "expected": [["Alice", "alice@mail.com"]],
    },
    {
        "description": "All merge into one",
        "run": lambda: len(solution([
            ["A", "a@b.com", "b@b.com"],
            ["A", "b@b.com", "c@b.com"]
        ])),
        "expected": 1,
    },
]
