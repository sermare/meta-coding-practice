from problems.p135_open_the_lock import solution

TEST_CASES = [
    {
        "description": "Standard BFS path",
        "run": lambda: solution(["0201","0101","0102","1212","2002"], "0202"),
        "expected": 6,
    },
    {
        "description": "Start is a deadend",
        "run": lambda: solution(["0000"], "8888"),
        "expected": -1,
    },
    {
        "description": "No deadends",
        "run": lambda: solution([], "0009"),
        "expected": 1,
    },
    {
        "description": "Impossible to reach",
        "run": lambda: solution(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"),
        "expected": -1,
    },
    {
        "description": "Target is start",
        "run": lambda: solution(["1234"], "0000"),
        "expected": 0,
    },
]
