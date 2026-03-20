from problems.p128_insert_delete_getrandom_o1 import solution

TEST_CASES = [
    {
        "description": "Insert and remove operations",
        "run": lambda: solution(
            ["RandomizedSet","insert","remove","insert"],
            [[],[1],[2],[2]]
        ),
        "expected": [None, True, False, True],
    },
    {
        "description": "Duplicate insert returns False",
        "run": lambda: solution(
            ["RandomizedSet","insert","insert"],
            [[],[1],[1]]
        ),
        "expected": [None, True, False],
    },
    {
        "description": "Remove then re-insert",
        "run": lambda: solution(
            ["RandomizedSet","insert","remove","insert"],
            [[],[5],[5],[5]]
        ),
        "expected": [None, True, True, True],
    },
    {
        "description": "GetRandom returns only element",
        "run": lambda: solution(
            ["RandomizedSet","insert","getRandom"],
            [[],[42],[]]
        ),
        "expected": [None, True, 42],
    },
]
