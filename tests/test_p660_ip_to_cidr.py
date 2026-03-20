from problems.p660_ip_to_cidr import solution

TEST_CASES = [
    {
        "description": "Basic case: 255.0.0.7, n=10",
        "run": lambda: solution("255.0.0.7", 10),
        "expected": ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"],
    },
    {
        "description": "Single IP: n=1",
        "run": lambda: solution("0.0.0.0", 1),
        "expected": ["0.0.0.0/32"],
    },
    {
        "description": "Two IPs: n=2",
        "run": lambda: solution("0.0.0.0", 2),
        "expected": ["0.0.0.0/31"],
    },
    {
        "description": "Power of two aligned: n=4",
        "run": lambda: solution("0.0.0.0", 4),
        "expected": ["0.0.0.0/30"],
    },
]
