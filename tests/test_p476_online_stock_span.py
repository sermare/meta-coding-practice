from problems.p476_online_stock_span import solution

TEST_CASES = [
    {
        "description": "Standard sequence",
        "run": lambda: solution(["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]),
        "expected": [None,1,1,1,2,1,4,6],
    },
    {
        "description": "All increasing",
        "run": lambda: solution(["StockSpanner","next","next","next"], [[],[1],[2],[3]]),
        "expected": [None,1,2,3],
    },
    {
        "description": "All decreasing",
        "run": lambda: solution(["StockSpanner","next","next","next"], [[],[3],[2],[1]]),
        "expected": [None,1,1,1],
    },
    {
        "description": "All same price",
        "run": lambda: solution(["StockSpanner","next","next","next"], [[],[5],[5],[5]]),
        "expected": [None,1,2,3],
    },
]
