from problems.p078_maximum_width_of_binary_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Standard tree: [1,3,2,5,3,null,9]",
        "run": lambda: solution(build_tree([1, 3, 2, 5, 3, None, 9])),
        "expected": 4,
    },
    {
        "description": "Left-skewed: [1,3,2,5]",
        "run": lambda: solution(build_tree([1, 3, 2, 5])),
        "expected": 2,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "Full binary tree: [1,2,3,4,5,6,7]",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, 6, 7])),
        "expected": 4,
    },
]
