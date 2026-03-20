from problems.p504_map_sum_pairs import solution

TEST_CASES = [
    {
        "description": "Basic insert and sum",
        "run": lambda: solution(["MapSum","insert","sum","insert","sum"], [[],["apple",3],["ap"],["app",2],["ap"]]),
        "expected": [None, None, 3, None, 5],
    },
    {
        "description": "Override key",
        "run": lambda: solution(["MapSum","insert","sum","insert","sum"], [[],["apple",3],["ap"],["apple",2],["ap"]]),
        "expected": [None, None, 3, None, 2],
    },
    {
        "description": "No prefix match",
        "run": lambda: solution(["MapSum","insert","sum"], [[],["apple",3],["b"]]),
        "expected": [None, None, 0],
    },
    {
        "description": "Empty prefix",
        "run": lambda: solution(["MapSum","insert","insert","sum"], [[],["a",1],["b",2],[""]]),
        "expected": [None, None, None, 3],
    },
]
