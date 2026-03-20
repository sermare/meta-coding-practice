from problems.p281_path_sum_iii import solution, build_tree

TEST_CASES = [
    {
        "description": "[10,5,-3,3,2,null,11,3,-2,null,1] targetSum=8 -> 3",
        "run": lambda: solution(build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8),
        "expected": 3,
    },
    {
        "description": "[5,4,8,11,null,13,4,7,2,null,null,5,1] targetSum=22 -> 3",
        "run": lambda: solution(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22),
        "expected": 3,
    },
    {
        "description": "Empty tree -> 0",
        "run": lambda: solution(build_tree([]), 0),
        "expected": 0,
    },
    {
        "description": "[1] targetSum=1 -> 1",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": 1,
    },
    {
        "description": "[1,-2,-3] targetSum=-1 -> 1",
        "run": lambda: solution(build_tree([1, -2, -3]), -1),
        "expected": 1,
    },
]
