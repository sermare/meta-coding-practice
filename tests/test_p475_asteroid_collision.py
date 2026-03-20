from problems.p475_asteroid_collision import solution

TEST_CASES = [
    {
        "description": "Right survives: [5,10,-5] -> [5,10]",
        "run": lambda: solution([5,10,-5]),
        "expected": [5,10],
    },
    {
        "description": "Both explode: [8,-8] -> []",
        "run": lambda: solution([8,-8]),
        "expected": [],
    },
    {
        "description": "Larger right: [10,2,-5] -> [10]",
        "run": lambda: solution([10,2,-5]),
        "expected": [10],
    },
    {
        "description": "No collision: [-2,-1,1,2]",
        "run": lambda: solution([-2,-1,1,2]),
        "expected": [-2,-1,1,2],
    },
    {
        "description": "Chain collision: [1,2,3,-4]",
        "run": lambda: solution([1,2,3,-4]),
        "expected": [-4],
    },
]
