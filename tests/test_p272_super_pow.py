from problems.p272_super_pow import solution

TEST_CASES = [
    {
        "description": "a=2, b=[3] -> 8",
        "run": lambda: solution(2, [3]),
        "expected": 8,
    },
    {
        "description": "a=2, b=[1,0] -> 1024",
        "run": lambda: solution(2, [1, 0]),
        "expected": 1024,
    },
    {
        "description": "a=1, b=[4,3,3,8,5,2] -> 1",
        "run": lambda: solution(1, [4, 3, 3, 8, 5, 2]),
        "expected": 1,
    },
    {
        "description": "a=2147483647, b=[2,0,0] -> 1198",
        "run": lambda: solution(2147483647, [2, 0, 0]),
        "expected": 1198,
    },
]
