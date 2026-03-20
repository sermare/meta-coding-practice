from problems.p216_assign_cookies import solution

TEST_CASES = [
    {
        "description": "Not enough cookies: g=[1,2,3] s=[1,1]",
        "run": lambda: solution([1, 2, 3], [1, 1]),
        "expected": 1,
    },
    {
        "description": "Enough cookies: g=[1,2] s=[1,2,3]",
        "run": lambda: solution([1, 2], [1, 2, 3]),
        "expected": 2,
    },
    {
        "description": "No cookies: g=[1,2] s=[]",
        "run": lambda: solution([1, 2], []),
        "expected": 0,
    },
    {
        "description": "No children: g=[] s=[1,2]",
        "run": lambda: solution([], [1, 2]),
        "expected": 0,
    },
    {
        "description": "All satisfied: g=[1,1] s=[1,1]",
        "run": lambda: solution([1, 1], [1, 1]),
        "expected": 2,
    },
]
