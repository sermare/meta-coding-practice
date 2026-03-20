from problems.p402_min_cost_climbing_stairs import solution

TEST_CASES = [
    {
        "description": "Simple three steps: [10,15,20]",
        "run": lambda: solution([10, 15, 20]),
        "expected": 15,
    },
    {
        "description": "Longer staircase: [1,100,1,1,1,100,1,1,100,1]",
        "run": lambda: solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
        "expected": 6,
    },
    {
        "description": "Two steps: [10,15]",
        "run": lambda: solution([10, 15]),
        "expected": 10,
    },
    {
        "description": "Equal costs: [5,5,5,5]",
        "run": lambda: solution([5, 5, 5, 5]),
        "expected": 10,
    },
    {
        "description": "Zero costs: [0,0,0,0]",
        "run": lambda: solution([0, 0, 0, 0]),
        "expected": 0,
    },
]
