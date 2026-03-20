from problems.p333_defanging_an_ip_address import solution

TEST_CASES = [
    {
        "description": "Basic: 1.1.1.1",
        "run": lambda: solution("1.1.1.1"),
        "expected": "1[.]1[.]1[.]1",
    },
    {
        "description": "Larger numbers: 255.100.50.0",
        "run": lambda: solution("255.100.50.0"),
        "expected": "255[.]100[.]50[.]0",
    },
    {
        "description": "Localhost: 127.0.0.1",
        "run": lambda: solution("127.0.0.1"),
        "expected": "127[.]0[.]0[.]1",
    },
    {
        "description": "All zeros: 0.0.0.0",
        "run": lambda: solution("0.0.0.0"),
        "expected": "0[.]0[.]0[.]0",
    },
]
