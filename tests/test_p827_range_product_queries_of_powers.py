from problems.p827_range_product_queries_of_powers import solution

TEST_CASES = [
    {
        "description": "n=15, multiple queries",
        "run": lambda: solution(15, [[0,1],[2,2],[0,3]]),
        "expected": [2, 4, 64],
    },
    {
        "description": "Power of 2: n=8, query=[0,0]",
        "run": lambda: solution(8, [[0,0]]),
        "expected": [8],
    },
    {
        "description": "n=2, single query",
        "run": lambda: solution(2, [[0,0]]),
        "expected": [2],
    },
    {
        "description": "n=7, full range",
        "run": lambda: solution(7, [[0,2]]),
        "expected": [8],
    },
]
