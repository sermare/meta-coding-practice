from problems.p039_powx_n import solution

TEST_CASES = [
    {
        "description": "2.0^10 -> 1024.0",
        "run": lambda: abs(solution(2.0, 10) - 1024.0) < 1e-5,
        "expected": True,
    },
    {
        "description": "2.1^3 -> 9.261",
        "run": lambda: abs(solution(2.1, 3) - 9.261) < 1e-5,
        "expected": True,
    },
    {
        "description": "2.0^-2 -> 0.25",
        "run": lambda: abs(solution(2.0, -2) - 0.25) < 1e-5,
        "expected": True,
    },
    {
        "description": "1.0^-2147483648 -> 1.0",
        "run": lambda: abs(solution(1.0, -2147483648) - 1.0) < 1e-5,
        "expected": True,
    },
    {
        "description": "0.00001^2147483647 -> 0.0",
        "run": lambda: abs(solution(0.00001, 2147483647) - 0.0) < 1e-5,
        "expected": True,
    },
]
