from problems.p270_reconstruct_itinerary import solution

TEST_CASES = [
    {
        "description": "Linear itinerary",
        "run": lambda: solution([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]),
        "expected": ["JFK","MUC","LHR","SFO","SJC"],
    },
    {
        "description": "Lexical ordering matters",
        "run": lambda: solution([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]),
        "expected": ["JFK","ATL","JFK","SFO","ATL","SFO"],
    },
    {
        "description": "Single ticket",
        "run": lambda: solution([["JFK","ATL"]]),
        "expected": ["JFK","ATL"],
    },
    {
        "description": "Round trip",
        "run": lambda: solution([["JFK","ATL"],["ATL","JFK"]]),
        "expected": ["JFK","ATL","JFK"],
    },
]
