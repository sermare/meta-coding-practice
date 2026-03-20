from problems.p290_ones_and_zeroes import solution

TEST_CASES = [
    {
        "description": '["10","0001","111001","1","0"] m=5 n=3 -> 4',
        "run": lambda: solution(["10", "0001", "111001", "1", "0"], 5, 3),
        "expected": 4,
    },
    {
        "description": '["10","0","1"] m=1 n=1 -> 2',
        "run": lambda: solution(["10", "0", "1"], 1, 1),
        "expected": 2,
    },
    {
        "description": '["0"] m=1 n=0 -> 1',
        "run": lambda: solution(["0"], 1, 0),
        "expected": 1,
    },
    {
        "description": '["111","1000","1000","1000"] m=9 n=3 -> 3',
        "run": lambda: solution(["111", "1000", "1000", "1000"], 9, 3),
        "expected": 3,
    },
]
