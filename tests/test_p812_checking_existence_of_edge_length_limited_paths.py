from problems.p812_checking_existence_of_edge_length_limited_paths import solution

TEST_CASES = [
    {
        "description": "Mixed results: n=3",
        "run": lambda: solution(3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]]),
        "expected": [False, True],
    },
    {
        "description": "Disconnected: n=5, no edges",
        "run": lambda: solution(5, [], [[0,1,10],[2,3,5]]),
        "expected": [False, False],
    },
    {
        "description": "All within limit: n=3, edges=[[0,1,1],[1,2,1]]",
        "run": lambda: solution(3, [[0,1,1],[1,2,1]], [[0,2,5]]),
        "expected": [True],
    },
    {
        "description": "Same node query: n=2",
        "run": lambda: solution(2, [[0,1,5]], [[0,0,1]]),
        "expected": [True],
    },
]
