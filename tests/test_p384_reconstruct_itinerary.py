from problems.p384_reconstruct_itinerary import solution


TEST_CASES = [
    {
        "description": "Standard itinerary",
        "run": lambda: solution([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
        "expected": ["JFK", "MUC", "LHR", "SFO", "SJC"],
    },
    {
        "description": "Multiple visits to same city",
        "run": lambda: solution([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]),
        "expected": ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
    },
    {
        "description": "Single ticket",
        "run": lambda: solution([["JFK", "AAA"]]),
        "expected": ["JFK", "AAA"],
    },
    {
        "description": "Lexical order matters",
        "run": lambda: solution([["JFK", "BBB"], ["JFK", "AAA"], ["AAA", "JFK"]]),
        "expected": ["JFK", "AAA", "JFK", "BBB"],
    },
]
