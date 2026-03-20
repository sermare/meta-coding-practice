from problems.p657_cheapest_flights_within_k_stops import solution

TEST_CASES = [
    {
        "description": "Basic case with k=1",
        "run": lambda: solution(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1),
        "expected": 700,
    },
    {
        "description": "Cheaper with more stops",
        "run": lambda: solution(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 2),
        "expected": 400,
    },
    {
        "description": "No route available",
        "run": lambda: solution(3, [[0,1,100],[1,2,100]], 0, 2, 0),
        "expected": -1,
    },
    {
        "description": "Direct flight",
        "run": lambda: solution(2, [[0,1,50]], 0, 1, 0),
        "expected": 50,
    },
]
