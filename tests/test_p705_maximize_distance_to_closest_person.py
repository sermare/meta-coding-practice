from problems.p705_maximize_distance_to_closest_person import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,0,0,0,1,0,1]",
        "run": lambda: solution([1, 0, 0, 0, 1, 0, 1]),
        "expected": 2,
    },
    {
        "description": "Person at end: [1,0,0,0]",
        "run": lambda: solution([1, 0, 0, 0]),
        "expected": 3,
    },
    {
        "description": "Person at start: [0,0,0,1]",
        "run": lambda: solution([0, 0, 0, 1]),
        "expected": 3,
    },
    {
        "description": "Adjacent seats: [1,0,1]",
        "run": lambda: solution([1, 0, 1]),
        "expected": 1,
    },
    {
        "description": "Large gap in middle: [1,0,0,0,0,0,0,1]",
        "run": lambda: solution([1, 0, 0, 0, 0, 0, 0, 1]),
        "expected": 3,
    },
]
