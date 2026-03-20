from problems.p366_house_robber_iii import solution, build_tree


TEST_CASES = [
    {
        "description": "Rob root and grandchildren: 7",
        "run": lambda: solution(build_tree([3, 2, 3, None, 3, None, 1])),
        "expected": 7,
    },
    {
        "description": "Rob children: 9",
        "run": lambda: solution(build_tree([3, 4, 5, 1, 3, None, 1])),
        "expected": 9,
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([5])),
        "expected": 5,
    },
    {
        "description": "Two levels",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": 5,
    },
]
