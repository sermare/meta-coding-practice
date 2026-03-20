from problems.p774_maximum_number_of_robots_within_budget import solution

TEST_CASES = [
    {
        "description": "Basic: budget=25",
        "run": lambda: solution([3,6,1,3,4], [2,1,3,4,5], 25),
        "expected": 3,
    },
    {
        "description": "All robots: budget=100",
        "run": lambda: solution([1,2,3], [1,1,1], 100),
        "expected": 3,
    },
    {
        "description": "No robots: budget=0",
        "run": lambda: solution([5,5,5], [5,5,5], 0),
        "expected": 0,
    },
    {
        "description": "Single robot: budget=10",
        "run": lambda: solution([11,3,5], [10,1,1], 10),
        "expected": 1,
    },
]
