from problems.p047_diameter_of_binary_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "[1,2,3,4,5] -> diameter 3",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5])),
        "expected": 3,
    },
    {
        "description": "[1,2] -> diameter 1",
        "run": lambda: solution(build_tree([1, 2])),
        "expected": 1,
    },
    {
        "description": "Single node -> diameter 0",
        "run": lambda: solution(build_tree([1])),
        "expected": 0,
    },
    {
        "description": "Empty tree -> diameter 0",
        "run": lambda: solution(build_tree([])),
        "expected": 0,
    },
    {
        "description": "[1,2,3,4,5,None,None,6] -> diameter 4",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, None, None, 6])),
        "expected": 4,
    },
]
