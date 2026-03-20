from problems.p798_strong_password_checker_ii import solution

TEST_CASES = [
    {
        "description": "Strong password: IloveLe3tcode!",
        "run": lambda: solution("IloveLe3tcode!"),
        "expected": True,
    },
    {
        "description": "Too short: Me+You",
        "run": lambda: solution("Me+You"),
        "expected": False,
    },
    {
        "description": "No special char: Abcdefg1",
        "run": lambda: solution("Abcdefg1"),
        "expected": False,
    },
    {
        "description": "Adjacent duplicates: aA1!aA1!aa",
        "run": lambda: solution("aA1!aA1!aa"),
        "expected": False,
    },
    {
        "description": "No uppercase: abcdef1!",
        "run": lambda: solution("abcdef1!"),
        "expected": False,
    },
]
