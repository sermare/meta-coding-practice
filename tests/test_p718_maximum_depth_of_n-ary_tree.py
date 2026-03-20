from problems.p718_maximum_depth_of_n-ary_tree import solution

TEST_CASES = [
    {
        "description": "Depth 3 tree",
        "run": lambda: solution([1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]),
        "expected": 3,
    },
    {
        "description": "Single node tree",
        "run": lambda: solution([1, []]),
        "expected": 1,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(None),
        "expected": 0,
    },
    {
        "description": "Depth 2 balanced tree",
        "run": lambda: solution([1, [[2, []], [3, []], [4, []]]]),
        "expected": 2,
    },
]
