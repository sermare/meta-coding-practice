from problems.p801_shortest_path_with_alternating_colors import solution

TEST_CASES = [
    {
        "description": "Red edges only: n=3, red=[[0,1],[1,2]], blue=[]",
        "run": lambda: solution(3, [[0,1],[1,2]], []),
        "expected": [0,1,-1],
    },
    {
        "description": "Blue edges only: n=3, red=[], blue=[[0,1],[1,2]]",
        "run": lambda: solution(3, [], [[0,1],[1,2]]),
        "expected": [0,1,-1],
    },
    {
        "description": "Alternating path available: n=3, red=[[0,1]], blue=[[1,2]]",
        "run": lambda: solution(3, [[0,1]], [[1,2]]),
        "expected": [0,1,2],
    },
    {
        "description": "Single node: n=1",
        "run": lambda: solution(1, [], []),
        "expected": [0],
    },
    {
        "description": "Both colors from start: n=3, red=[[0,1],[0,2]], blue=[[0,1],[0,2]]",
        "run": lambda: solution(3, [[0,1],[0,2]], [[0,1],[0,2]]),
        "expected": [0,1,1],
    },
]
