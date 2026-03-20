from problems.p786_maximum_total_importance_of_roads import solution

TEST_CASES = [
    {
        "description": "Basic: n=5, 6 roads",
        "run": lambda: solution(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]),
        "expected": 43,
    },
    {
        "description": "No roads: n=3",
        "run": lambda: solution(3, []),
        "expected": 0,
    },
    {
        "description": "Single road: n=2, [[0,1]]",
        "run": lambda: solution(2, [[0,1]]),
        "expected": 3,
    },
    {
        "description": "Star graph: n=4, [[0,1],[0,2],[0,3]]",
        "run": lambda: solution(4, [[0,1],[0,2],[0,3]]),
        "expected": 18,
    },
]
