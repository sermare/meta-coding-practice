from problems.p444_restore_ip_addresses import solution

TEST_CASES = [
    {
        "description": "Basic: 25525511135",
        "run": lambda: sorted(solution("25525511135")),
        "expected": sorted(["255.255.11.135", "255.255.111.35"]),
    },
    {
        "description": "Zeros: 0000",
        "run": lambda: solution("0000"),
        "expected": ["0.0.0.0"],
    },
    {
        "description": "Ones: 1111",
        "run": lambda: solution("1111"),
        "expected": ["1.1.1.1"],
    },
    {
        "description": "Too short: 11",
        "run": lambda: solution("11"),
        "expected": [],
    },
    {
        "description": "Multiple results: 101023",
        "run": lambda: sorted(solution("101023")),
        "expected": sorted(["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    },
]
