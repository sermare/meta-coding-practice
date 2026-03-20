from problems.p079_accounts_merge import solution

TEST_CASES = [
    {
        "description": "Merge accounts with shared emails",
        "run": lambda: sorted(solution([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])),
        "expected": sorted([["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]),
    },
    {
        "description": "No merges needed",
        "run": lambda: sorted(solution([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"]])),
        "expected": sorted([["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"]]),
    },
    {
        "description": "Single account",
        "run": lambda: solution([["Alice", "alice@mail.com"]]),
        "expected": [["Alice", "alice@mail.com"]],
    },
    {
        "description": "All merge into one",
        "run": lambda: solution([["A", "a@b.com", "c@d.com"], ["A", "c@d.com", "e@f.com"]]),
        "expected": [["A", "a@b.com", "c@d.com", "e@f.com"]],
    },
]
