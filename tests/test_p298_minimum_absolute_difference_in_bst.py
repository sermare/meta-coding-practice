from problems.p298_minimum_absolute_difference_in_bst import solution, build_tree

TEST_CASES = [
    {
        "description": "[4,2,6,1,3] -> 1",
        "run": lambda: solution(build_tree([4, 2, 6, 1, 3])),
        "expected": 1,
    },
    {
        "description": "[1,0,48,None,None,12,49] -> 1",
        "run": lambda: solution(build_tree([1, 0, 48, None, None, 12, 49])),
        "expected": 1,
    },
    {
        "description": "[236,104,701,None,227,None,911] -> 9",
        "run": lambda: solution(build_tree([236, 104, 701, None, 227, None, 911])),
        "expected": 9,
    },
    {
        "description": "[1,None,3] -> 2",
        "run": lambda: solution(build_tree([1, None, 3])),
        "expected": 2,
    },
    {
        "description": "[5,4,7] -> 1",
        "run": lambda: solution(build_tree([5, 4, 7])),
        "expected": 1,
    },
]
