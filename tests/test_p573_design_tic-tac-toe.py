from problems.p573_design_tic-tac-toe import solution

TEST_CASES = [
    {
        "description": "Player 1 wins diagonal",
        "run": lambda: solution(3, [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]),
        "expected": [0, 0, 0, 0, 0, 0, 1],
    },
    {
        "description": "Player 2 wins row",
        "run": lambda: solution(3, [[0, 0, 1], [1, 0, 2], [0, 1, 1], [1, 1, 2], [2, 2, 1], [1, 2, 2]]),
        "expected": [0, 0, 0, 0, 0, 2],
    },
    {
        "description": "2x2 board quick win",
        "run": lambda: solution(2, [[0, 0, 1], [1, 0, 2], [0, 1, 1]]),
        "expected": [0, 0, 1],
    },
    {
        "description": "No winner yet",
        "run": lambda: solution(3, [[0, 0, 1], [1, 1, 2]]),
        "expected": [0, 0],
    },
]
