from problems.p629_find_the_celebrity import solution

TEST_CASES = [
    {
        "description": "Person 1 is celebrity",
        "run": lambda: solution(
            lambda a, b, g=[[1, 1, 0], [0, 1, 0], [1, 1, 1]]: g[a][b] == 1,
            3
        ),
        "expected": 1,
    },
    {
        "description": "No celebrity",
        "run": lambda: solution(
            lambda a, b, g=[[1, 0, 1], [1, 1, 0], [0, 1, 1]]: g[a][b] == 1,
            3
        ),
        "expected": -1,
    },
    {
        "description": "Two people, person 1 celebrity",
        "run": lambda: solution(
            lambda a, b, g=[[1, 1], [0, 1]]: g[a][b] == 1,
            2
        ),
        "expected": 1,
    },
    {
        "description": "Single person",
        "run": lambda: solution(
            lambda a, b, g=[[1]]: g[a][b] == 1,
            1
        ),
        "expected": 0,
    },
]
