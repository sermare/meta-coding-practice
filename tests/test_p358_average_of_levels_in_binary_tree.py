from problems.p358_average_of_levels_in_binary_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree averages",
        "run": lambda: solution(build_tree([3, 9, 20, None, None, 15, 7])),
        "expected": [3.0, 14.5, 11.0],
    },
    {
        "description": "Complete tree averages",
        "run": lambda: solution(build_tree([3, 9, 20, 15, 7])),
        "expected": [3.0, 14.5, 11.0],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": [1.0],
    },
    {
        "description": "Two levels",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": [1.0, 2.5],
    },
]
