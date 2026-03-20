from problems.p395_loud_and_rich import solution


TEST_CASES = [
    {
        "description": "Standard richer/quiet graph",
        "run": lambda: solution([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]),
        "expected": [5, 5, 2, 5, 4, 5, 6, 7],
    },
    {
        "description": "Single person",
        "run": lambda: solution([], [0]),
        "expected": [0],
    },
    {
        "description": "No richer relationships",
        "run": lambda: solution([], [2, 1, 0]),
        "expected": [0, 1, 2],
    },
    {
        "description": "Simple chain: a > b > c",
        "run": lambda: solution([[0, 1], [1, 2]], [2, 0, 1]),
        "expected": [0, 1, 1],
    },
]
