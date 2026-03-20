from problems.p025_decode_ways import solution

TEST_CASES = [
    {
        "description": "'12' can be decoded 2 ways (AB or L)",
        "run": lambda: solution("12"),
        "expected": 2,
    },
    {
        "description": "'226' can be decoded 3 ways",
        "run": lambda: solution("226"),
        "expected": 3,
    },
    {
        "description": "'06' cannot be decoded (leading zero)",
        "run": lambda: solution("06"),
        "expected": 0,
    },
    {
        "description": "'11106' can be decoded 2 ways",
        "run": lambda: solution("11106"),
        "expected": 2,
    },
    {
        "description": "'10' can be decoded 1 way (J)",
        "run": lambda: solution("10"),
        "expected": 1,
    },
]
