from problems.p802_maximum_level_sum_of_a_binary_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Max at level 2: [1,7,0,7,-8]",
        "run": lambda: solution(build_tree([1, 7, 0, 7, -8])),
        "expected": 2,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "Max at root: [10,1,2]",
        "run": lambda: solution(build_tree([10, 1, 2])),
        "expected": 1,
    },
    {
        "description": "Negative values: [-1,-2,-3,4,5]",
        "run": lambda: solution(build_tree([-1, -2, -3, 4, 5])),
        "expected": 3,
    },
]
