from problems.p300_diameter_of_binary_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Left-skewed tree [1,2,None,3,None,4] -> 3",
        "run": lambda: solution(build_tree([1, 2, None, 3, None, 4])),
        "expected": 3,
    },
    {
        "description": "Right-skewed tree [1,None,2,None,3] -> 2",
        "run": lambda: solution(build_tree([1, None, 2, None, 3])),
        "expected": 2,
    },
    {
        "description": "Balanced [1,2,3,4,5,6,7] -> 4",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, 6, 7])),
        "expected": 4,
    },
    {
        "description": "Diameter not through root [1,2,3,4,5,None,None,6,None,None,7,8] -> 5",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8])),
        "expected": 5,
    },
    {
        "description": "Empty tree -> 0",
        "run": lambda: solution(build_tree([])),
        "expected": 0,
    },
]
