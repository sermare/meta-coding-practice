from problems.p028_word_search import solution

_BOARD = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]

TEST_CASES = [
    {
        "description": "Find 'ABCCED' in 3x4 board -> True",
        "run": lambda: solution([row[:] for row in _BOARD], "ABCCED"),
        "expected": True,
    },
    {
        "description": "Find 'SEE' in 3x4 board -> True",
        "run": lambda: solution([row[:] for row in _BOARD], "SEE"),
        "expected": True,
    },
    {
        "description": "Find 'ABCB' in 3x4 board -> False (can't reuse cell)",
        "run": lambda: solution([row[:] for row in _BOARD], "ABCB"),
        "expected": False,
    },
    {
        "description": "Single cell board with matching letter -> True",
        "run": lambda: solution([["a"]], "a"),
        "expected": True,
    },
    {
        "description": "Find 'ABDC' in 2x2 board -> True",
        "run": lambda: solution([["A", "B"], ["C", "D"]], "ABDC"),
        "expected": True,
    },
]
