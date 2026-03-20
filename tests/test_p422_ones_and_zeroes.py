from problems.p422_ones_and_zeroes import solution

TEST_CASES = [
    {
        "description": "Basic: strs=['10','0001','111001','1','0'] m=5 n=3",
        "run": lambda: solution(["10", "0001", "111001", "1", "0"], 5, 3),
        "expected": 4,
    },
    {
        "description": "Small: strs=['10','0','1'] m=1 n=1",
        "run": lambda: solution(["10", "0", "1"], 1, 1),
        "expected": 2,
    },
    {
        "description": "Single string: strs=['11'] m=2 n=0",
        "run": lambda: solution(["11"], 2, 0),
        "expected": 0,
    },
    {
        "description": "All fit: strs=['0','1'] m=1 n=1",
        "run": lambda: solution(["0", "1"], 1, 1),
        "expected": 2,
    },
    {
        "description": "Empty strs: strs=[] m=5 n=3",
        "run": lambda: solution([], 5, 3),
        "expected": 0,
    },
]
