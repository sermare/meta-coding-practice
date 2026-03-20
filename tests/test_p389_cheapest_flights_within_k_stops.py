from problems.p389_cheapest_flights_within_k_stops import solution


TEST_CASES = [
    {
        "description": "Cheapest with 1 stop: 700",
        "run": lambda: solution(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1),
        "expected": 700,
    },
    {
        "description": "Two-hop cheaper: 200",
        "run": lambda: solution(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),
        "expected": 200,
    },
    {
        "description": "Zero stops: direct only 500",
        "run": lambda: solution(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),
        "expected": 500,
    },
    {
        "description": "No route possible",
        "run": lambda: solution(3, [[0,1,100]], 0, 2, 1),
        "expected": -1,
    },
]
